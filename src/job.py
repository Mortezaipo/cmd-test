"""Job handler.

Job works with commands and command generator to build and manage
commands in seperated threads.
"""
from builder import Builder
from command import Command


class Job:
    """Job handler class."""

    def __init__(self, command, thread, io, priority):
        """Initialize Job class."""
        self._commands = []
        self._generated_commands = Builder(command, thread).generate()
        for cmd_string in self._generated_commands:
            new_cmd = Command(cmd_string, 1, io, priority)

            # prepare connection between command nodes
            if self._commands:
                last_cmd = self._commands[-1]
                last_cmd.set_next(new_cmd)
                new_cmd.set_prev(last_cmd)

            self._commands.append(new_cmd)

    def add_new_job(self, command_node):
        pass

    def pause_job(self, command_node):
        pass

    def del_job(self, command_node):
        pass

    def duplicate_job(self, command_node):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    @property
    def status(self):
        """Get current status."""
        return self._status

    @status.setter
    def status(self, new_status):
        """Set new status."""
        self._status = new_status
