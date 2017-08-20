"""Command data structure.

Each command has its own data field and it has access to the next
generated command.
"""


class Command:
    """Command node class."""

    def __init__(self, command: str, process: int, thread: int, io: list, priority: int):
        """Initialize Command class."""

        # data field
        self._command = command
        self._process = process
        self._thread = thread
        self._io = io
        self._priority = priority
        self._is_in_process = False

        # node access
        self._next = None
        self._prev = None

    def __repr__(self):
        """Return repr(self)."""
        return '<Command Object ID:{} Priority:{} Status:{}>'.format(id(self), self._priority, self._status)

    def __str__(self):
        """Return str(self)."""
        return "Command:{} Status:{}".format(self._command, self._status)

    @property
    def command(self):
        """Return command string."""
        return self._command

    @property
    def process(self):
        """Return total process."""
        return self._process

    @property
    def thread(self):
        """Return total thread."""
        return self._thread

    @property
    def io(self):
        """Return list of input/output."""
        return self._io

    @property
    def priority(self):
        """Return command priority."""
        return self._priority

    @property
    def is_in_process(self):
        """Get command status."""
        return self._is_in_process

    @is_in_process.setter
    def is_in_process(self, new_state: bool):
        """Set new status on command."""
        self._is_in_process = new_state

    @property
    def who_is_next(self):
        """Return next command."""
        return self._next

    @property
    def who_is_prev(self):
        """Return previous command."""
        return self._prev
