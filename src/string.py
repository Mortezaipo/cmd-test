"""Main string library to generate and check strings."""
import re

import rstr

import show
import const


class Strings:
    """Strings methods to generate strings and test match for reverse check."""

    @staticmethod
    def generator(pattern, length=0):
        """Generate string based on regex pattern.

        :param pattern: regex pattern
        :param length: result length
        :type pattern: str
        :type length: int
        :return: generated string
        :rtype: string
        """
        try:
            re.compile(pattern)
        except re.error:
            show.fprint(const.ERROR, 1,
                        "Invalid regex pattern: {}".format(pattern))
        length = len(pattern) if length == 0 else length
        return rstr.rstr(pattern, length)

    @staticmethod
    def match(pattern, text):
        """Check string with pattern.

        :param pattern: regex pattern
        :param text: entry string
        :type pattern: str
        :type text: str
        :return: is pattern matched with text or not (boolean result).
        :rtype: bool
        """
        if re.match(pattern, text):
            return True
        return False
