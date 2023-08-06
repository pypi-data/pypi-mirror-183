"""Create a tmux workspace from a workspace :py:obj:`dict`.

tmuxp.workspace.builder
~~~~~~~~~~~~~~~~~~~~~~~

"""
import logging
import time

from libtmux.common import has_lt_version
from libtmux.exc import TmuxSessionExists
from libtmux.pane import Pane
from libtmux.server import Server
from libtmux.session import Session
from libtmux.window import Window

from .. import exc
from ..util import get_current_pane, run_before_script

logger = logging.getLogger(__name__)

DEFAULT_WIDTH = "800"
DEFAULT_HEIGHT = "600"
DEFAULT_SIZE = f"{DEFAULT_WIDTH}x{DEFAULT_HEIGHT}"


class WorkspaceBuilder:

    """
    Load workspace from session :py:obj:`dict`.

    Build tmux workspace from a configuration. Creates and names windows, sets
    options, splits windows into panes.

    Examples
    --------

    >>> import yaml

    >>> session_config = yaml.load('''
    ...     session_name: sample workspace
    ...     start_directory: '~'
    ...     windows:
    ...     - window_name: editor
    ...       layout: main-vertical
    ...       panes:
    ...       - shell_command:
    ...         - cmd: vim
    ...       - shell_command:
    ...         - cmd: echo "hey"
    ...
    ...     - window_name: logging
    ...       panes:
    ...       - shell_command:
    ...         - cmd: tail | echo 'hi'
    ...
    ...     - window_name: test
    ...       panes:
    ...       - shell_command:
    ...         - cmd: htop
    ... ''', Loader=yaml.Loader)

    >>> builder = WorkspaceBuilder(sconf=session_config, server=server)

    **New session:**

    >>> builder.build()

    >>> new_session = builder.session

    >>> new_session.name == 'sample workspace'
    True

    >>> len(new_session.windows)
    3

    >>> sorted([window.name for window in new_session.windows])
    ['editor', 'logging', 'test']

    **Existing session:**

    >>> len(session.windows)
    1

    >>> builder.build(session=session)

    _Caveat:_ Preserves old session name:

    >>> session.name == 'sample workspace'
    False

    >>> len(session.windows)
    3

    >>> sorted([window.name for window in session.windows])
    ['editor', 'logging', 'test']

    The normal phase of loading is:

    1. Load JSON / YAML file via via :class:`pathlib.Path`::

           from tmuxp import config_reader
           sconf = config_reader.ConfigReader._load(raw_yaml)

       The reader automatically detects the file type from :attr:`pathlib.suffix`.

       We can also parse raw file::

           import pathlib
           from tmuxp import config_reader

           sconf = config_reader.ConfigReader._from_file(
               pathlib.Path('path/to/config.yaml')
           )

    2. :meth:`config.expand` sconf inline shorthand::

           from tmuxp import config
           sconf = config.expand(sconf)

    3. :meth:`config.trickle` passes down default values from session
       -> window -> pane if applicable::

           sconf = config.trickle(sconf)

    4. (You are here) We will create a :class:`libtmux.Session` (a real
       ``tmux(1)`` session) and iterate through the list of windows, and
       their panes, returning full :class:`libtmux.Window` and
       :class:`libtmux.Pane` objects each step of the way::

           workspace = WorkspaceBuilder(sconf=sconf)

    It handles the magic of cases where the user may want to start
    a session inside tmux (when `$TMUX` is in the env variables).
    """

    def __init__(self, sconf, plugins=[], server=None):
        """
        Initialize workspace loading.

        Parameters
        ----------
        sconf : dict
            session config, includes a :py:obj:`list` of ``windows``.

        plugins : list
            plugins to be used for this session

        server : :class:`libtmux.Server`
            tmux server to build session in

        Notes
        -----
        TODO: Initialize :class:`libtmux.Session` from here, in
        ``self.session``.
        """

        if not sconf:
            raise exc.EmptyWorkspaceException("session configuration is empty.")

        # validation.validate_schema(sconf)

        if isinstance(server, Server):
            self.server = server
        else:
            self.server = None

        self.sconf = sconf

        self.plugins = plugins

    def session_exists(self, session_name=None):
        exists = self.server.has_session(session_name)
        if not exists:
            return exists

        try:
            self.session = self.server.sessions.filter(session_name=session_name)[0]
        except IndexError:
            return False
        return True

    def build(self, session=None, append=False):
        """
        Build tmux workspace in session.

        Optionally accepts ``session`` to build with only session object.

        Without ``session``, it will use :class:`libmtux.Server` at
        ``self.server`` passed in on initialization to create a new Session
        object.

        Parameters
        ----------
        session : :class:`libtmux.Session`
            session to build workspace in
        append : bool
            append windows in current active session
        """

        if not session:
            if not self.server:
                raise exc.TmuxpException(
                    "WorkspaceBuilder.build requires server to be passed "
                    + "on initialization, or pass in session object to here."
                )

            if self.server.has_session(self.sconf["session_name"]):
                try:
                    self.session = self.server.sessions.filter(
                        session_name=self.sconf["session_name"]
                    )[0]

                    raise TmuxSessionExists(
                        "Session name %s is already running."
                        % self.sconf["session_name"]
                    )
                except IndexError:
                    pass
            else:
                new_session_kwargs = {}
                if "start_directory" in self.sconf:
                    new_session_kwargs["start_directory"] = self.sconf[
                        "start_directory"
                    ]
                session = self.server.new_session(
                    session_name=self.sconf["session_name"],
                    **new_session_kwargs,
                )

            assert self.sconf["session_name"] == session.name
            assert len(self.sconf["session_name"]) > 0

        self.session = session
        self.server = session.server

        self.server.sessions
        assert self.server.has_session(session.name)
        assert session.id

        assert isinstance(session, Session)

        for plugin in self.plugins:
            plugin.before_workspace_builder(self.session)

        focus = None

        if "before_script" in self.sconf:
            try:
                cwd = None

                # we want to run the before_script file cwd'd from the
                # session start directory, if it exists.
                if "start_directory" in self.sconf:
                    cwd = self.sconf["start_directory"]
                run_before_script(self.sconf["before_script"], cwd=cwd)
            except Exception as e:
                self.session.kill_session()
                raise e
        if "options" in self.sconf:
            for option, value in self.sconf["options"].items():
                self.session.set_option(option, value)
        if "global_options" in self.sconf:
            for option, value in self.sconf["global_options"].items():
                self.session.set_option(option, value, _global=True)
        if "environment" in self.sconf:
            for option, value in self.sconf["environment"].items():
                self.session.set_environment(option, value)

        for w, wconf in self.iter_create_windows(session, append):
            assert isinstance(w, Window)

            for plugin in self.plugins:
                plugin.on_window_create(w)

            focus_pane = None
            for p, pconf in self.iter_create_panes(w, wconf):
                assert isinstance(p, Pane)
                p = p

                if "layout" in wconf:
                    w.select_layout(wconf["layout"])

                if "focus" in pconf and pconf["focus"]:
                    focus_pane = p

            if "focus" in wconf and wconf["focus"]:
                focus = w

            self.config_after_window(w, wconf)

            for plugin in self.plugins:
                plugin.after_window_finished(w)

            if focus_pane:
                focus_pane.select_pane()

        if focus:
            focus.select_window()

    def iter_create_windows(self, session, append=False):
        """
        Return :class:`libtmux.Window` iterating through session config dict.

        Generator yielding :class:`libtmux.Window` by iterating through
        ``sconf['windows']``.

        Applies ``window_options`` to window.

        Parameters
        ----------
        session : :class:`libtmux.Session`
            session to create windows in
        append : bool
            append windows in current active session

        Returns
        -------
        tuple of (:class:`libtmux.Window`, ``wconf``)
            Newly created window, and the section from the tmuxp configuration
            that was used to create the window.
        """
        for i, wconf in enumerate(self.sconf["windows"], start=1):
            if "window_name" not in wconf:
                window_name = None
            else:
                window_name = wconf["window_name"]

            is_first_window_pass = self.first_window_pass(i, session, append)

            w1 = None
            if is_first_window_pass:  # if first window, use window 1
                w1 = session.attached_window
                w1.move_window(99)

            if "start_directory" in wconf:
                sd = wconf["start_directory"]
            else:
                sd = None

            # If the first pane specifies a start_directory, use that instead.
            panes = wconf["panes"]
            if panes and "start_directory" in panes[0]:
                sd = panes[0]["start_directory"]

            if "window_shell" in wconf:
                ws = wconf["window_shell"]
            else:
                ws = None

            # If the first pane specifies a shell, use that instead.
            try:
                if wconf["panes"][0]["shell"] != "":
                    ws = wconf["panes"][0]["shell"]
            except (KeyError, IndexError):
                pass

            environment = panes[0].get("environment", wconf.get("environment"))
            if environment and has_lt_version("3.0"):
                # Falling back to use the environment of the first pane for the window
                # creation is nice but yields misleading error messages.
                pane_env = panes[0].get("environment")
                win_env = wconf.get("environment")
                if pane_env and win_env:
                    target = "panes and windows"
                elif pane_env:
                    target = "panes"
                else:
                    target = "windows"
                logging.warning(
                    f"Cannot set environment for new {target}. "
                    "You need tmux 3.0 or newer for this."
                )
                environment = None

            w = session.new_window(
                window_name=window_name,
                start_directory=sd,
                attach=False,  # do not move to the new window
                window_index=wconf.get("window_index", ""),
                window_shell=ws,
                environment=environment,
            )

            if is_first_window_pass:  # if first window, use window 1
                session.attached_window.kill_window()

            assert isinstance(w, Window)
            if "options" in wconf and isinstance(wconf["options"], dict):
                for key, val in wconf["options"].items():
                    w.set_window_option(key, val)

            if "focus" in wconf and wconf["focus"]:
                w.select_window()

            yield w, wconf

    def iter_create_panes(self, w, wconf):
        """
        Return :class:`libtmux.Pane` iterating through window config dict.

        Run ``shell_command`` with ``$ tmux send-keys``.

        Parameters
        ----------
        w : :class:`libtmux.Window`
            window to create panes for
        wconf : dict
            config section for window

        Returns
        -------
        tuple of (:class:`libtmux.Pane`, ``pconf``)
            Newly created pane, and the section from the tmuxp configuration
            that was used to create the pane.
        """
        assert isinstance(w, Window)

        pane_base_index = int(w.show_window_option("pane-base-index", g=True))

        p = None

        for pindex, pconf in enumerate(wconf["panes"], start=pane_base_index):
            if pindex == int(pane_base_index):
                p = w.attached_pane
            else:

                def get_pane_start_directory():
                    if "start_directory" in pconf:
                        return pconf["start_directory"]
                    elif "start_directory" in wconf:
                        return wconf["start_directory"]
                    else:
                        return None

                def get_pane_shell():
                    if "shell" in pconf:
                        return pconf["shell"]
                    elif "window_shell" in wconf:
                        return wconf["window_shell"]
                    else:
                        return None

                environment = pconf.get("environment", wconf.get("environment"))
                if environment and has_lt_version("3.0"):
                    # Just issue a warning when the environment comes from the pane
                    # configuration as a warning for the window was already issued when
                    # the window was created.
                    if pconf.get("environment"):
                        logging.warning(
                            "Cannot set environment for new panes. "
                            "You need tmux 3.0 or newer for this."
                        )
                    environment = None

                p = w.split_window(
                    attach=True,
                    start_directory=get_pane_start_directory(),
                    shell=get_pane_shell(),
                    target=p.id,
                    environment=environment,
                )

            assert isinstance(p, Pane)
            if "layout" in wconf:
                w.select_layout(wconf["layout"])

            if "suppress_history" in pconf:
                suppress = pconf["suppress_history"]
            elif "suppress_history" in wconf:
                suppress = wconf["suppress_history"]
            else:
                suppress = True

            enter = pconf.get("enter", True)
            sleep_before = pconf.get("sleep_before", None)
            sleep_after = pconf.get("sleep_after", None)
            for cmd in pconf["shell_command"]:
                enter = cmd.get("enter", enter)
                sleep_before = cmd.get("sleep_before", sleep_before)
                sleep_after = cmd.get("sleep_after", sleep_after)

                if sleep_before is not None:
                    time.sleep(sleep_before)

                p.send_keys(cmd["cmd"], suppress_history=suppress, enter=enter)

                if sleep_after is not None:
                    time.sleep(sleep_after)

            if "focus" in pconf and pconf["focus"]:
                assert p.pane_id is not None
                w.select_pane(p.pane_id)

            yield p, pconf

    def config_after_window(self, w, wconf):
        """Actions to apply to window after window and pane finished.

        When building a tmux session, sometimes its easier to postpone things
        like setting options until after things are already structurally
        prepared.

        Parameters
        ----------
        w : :class:`libtmux.Window`
            window to create panes for
        wconf : dict
            config section for window
        """
        if "options_after" in wconf and isinstance(wconf["options_after"], dict):
            for key, val in wconf["options_after"].items():
                w.set_window_option(key, val)

    def find_current_attached_session(self):
        current_active_pane = get_current_pane(self.server)

        if not current_active_pane:
            raise exc.TmuxpException("No session active.")

        return next(
            (
                s
                for s in self.server.sessions
                if s.session_id == current_active_pane.session_id
            ),
            None,
        )

    def first_window_pass(self, i, session, append):
        return len(session.windows) == 1 and i == 1 and not append
