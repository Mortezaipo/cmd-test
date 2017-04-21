#!/usr/bin/env python
"""
                        .CMD TEST.

Copyright (C) 2016  Morteza Nourelahi Alamdari (Mortezaipo)
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
from src import lib
from src import show
from src import const
from src import dispatch


def main(args: list):
    """Main method to start tests.

    :param args: list of entered arguments
    :type args: list
    :return: void
    :rtype: void
    """
    if not lib.is_file_exists(args[0]):
        show.fprint(const.ERROR, 2, "Config file not found.")

    if not lib.has_file_read_permission(args[0]):
        show.fprint(const.ERROR, 3, "Config file doesn't have read permission.")

    config = lib.load_config_file(args[0])
    if not config:
        show.fprint(const.ERROR, 4, "Config file content is not valid.")

    check_result = lib.validate_config_structure(config)
    if check_result is not True:
        show.fprint(const.ERROR, -1, "Config file structure is not valid.")
        show.fprint(const.ERROR, 5, "***ERROR***", check_result[1])

    show.fprint(const.INFO, -1, "cmd-test started...")
    lib.dispatch.start(config)

if __name__ == "__main__":
    if len(sys.args) == 0:
        fprint(consts.ERROR, 1, "Need config file address as first parameter.")
    main(sys.args)
