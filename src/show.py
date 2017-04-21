"""Print outputs and results."""

import sys

from colorclass import Color
from terminaltables import AsciiTable


def fprint(mode, exit_code=-1, *msg):
    """Print output with style and exit code if required.

    :param mode: output text color. Accessible in config.py.
    :param exit_code: If it needs to exit current process. -1 means no exit.
    :param msg: list of all messages. All messages will be convert to string.
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


def tprint(subject, exit_code=-1, *msg):
    """Print output in table style and exit code if required.

    :param exit_code: If it needs to exit current process. -1 means no exit.
    :param msg: List of all messages. All messages will be convert to string.
    :type exit_code: int
    :type msg: dict
    :return: void
    :rtype: void
    """
    print(AsciiTable(msg).table)
    if exit_code >= 0:
        sys.exit(exit_code)
