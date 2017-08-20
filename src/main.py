import json
import sys


road_file_path = "myconf.json"


### Command Node Structure
class Command:
    def __init__(self, command, process, thread, io, priority):
        # Data field
        self._command = command
        self._process = process
        self._thread = thread
        self._io = io
        self._priority = priority

        # Node access fields
        self._next = None
        self._prev = None

    def __repr__(self):
        pass

    def __str__(self):
        pass


### Jobs which should create pattern and run commands
class Job:
    def __init__(self, command, process, thread, io, priority):
        self._command = []
        self._command.append(Command(command, process, thread, io, priority))

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


### Process which should run jobs in new thread
class Process:
    def __init__(self, name):
        self._name = name

    def add_new_child(self, job):
        pass

    def add_new_process_child(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


def main():
    road_file = open(road_file_path, "r").read()

    try:
        road_plan = json.loads(road_file)
    except:
        sys.exit(1)

    for action in road_plan["actions"]:
        Job(action["command"], action["process"], action["thread"], action["io"], action["priority"])


if __name__ == "__main__":
    main()
