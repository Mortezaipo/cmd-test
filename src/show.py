"""Print outputs and results."""
from colorclass import Color
import sys


def fprint(mode, exit_code, *msg):
    """Print output with style and exit code if required.

    :param mode: output text color. Accessible in config.py.
    :param exit_code: If it needs to exit current process. -1 means no exit.
    :param msg: list of all messages. All messages will convert to string.
    :type mode: str
    :type exit_code: int
    :type msg: any
    :return: void
    :rtype: void
    """
    text = " ".join([x for x in map(str, msg)])
    print(Color(mode % text))
    if exit_code >= 0:
        sys.exit(exit_code)
