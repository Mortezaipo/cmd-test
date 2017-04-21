"""Application constant variables."""

# Output colors
ERROR = "{autored}%s{/autored}"
SUCCESS = "{autogreen}%s{/autogreen}"
INFO = "{autocyan}%s{/autocyan}"

# Error types
#=====================================================#
#  NOT FOUND  #  INVALID TYPE   #  INVALID STRUCTURE  #
#=====================================================#
ACTION_KEY_NOT_FOUND = (100, "'actions' key not found")
ACTION_VALUE_INVALID_TYPE = (110, "Action value must be list")
ACTION_VALUE_IS_EMPTY = (101, "Action value is empty")

COMMAND_KEY_NOT_FOUND = (200, "'command' key not found")
COMMAND_VALUE_INVALID_TYPE = (210, "'command' value must be string")
COMMAND_VALUE_IS_EMPTY = (201, "'command' value is empty")

PROCESS_KEY_NOT_FOUND = (300, "'process' key not found")
PROCESS_VALUE_INVALID_TYPE = (310, "'process' value must be integer")
PROCESS_VALUE_IS_EMPTY = (301, "'process' value is empty")
PROCESS_VALUE_INVALID_VALUE = (302, "'process' value must be positive and integer and greater than zero")

THREAD_KEY_NOT_FOUND = (400, "'thread' key not found")
THREAD_VALUE_INVALID_TYPE = (410, "'thread' value must be integer")
THREAD_VALUE_IS_EMPTY = (401, "'thread' value is empty")
THREAD_VALUE_INVALID_VALUE = (402, "'thread' value must be positive and integer and greater than zero")

IO_KEY_NOT_FOUND = (500, "'io' key not found")
IO_VALUE_INVALID_TYPE = (510, "'io' value must be list")
IO_VALUE_IS_EMPTY = (501, "'io' value is empty")
IO_VALUE_INVALID_VALUE = (502, "'io' value must be have correct pattern")
IO_VALUE_THREAD_NOT_FOUND = (503, "'io' value wants to connect to a thread which doesn't exists")
IO_VALUE_PROCESS_NOT_FOUND = (503, "'io' value wants to connect to a process which doesn't exists")
