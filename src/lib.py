"""Extra library."""

import os
import socket
import re
import json

import const


def is_file_exists(path: str):
    """Check file existance.

    :param path: file address
    :type path: str
    :return: Checking file existance
    :rtype: bool
    """
    if os.path.exists(path):
        return True
    return False


def has_file_read_permission(path: str):
    """Check file read permission.

    :param path: file address
    :type path: str
    :return: Checking file read permission
    :rtype: bool
    """
    if os.access(path, os.R_OK):
        return True
    return False


def is_rpc_addr_establish(addr: str):
    """Check RPC addr connection.

    :param addr: Connection address
    :type addr: str
    :return: Checking connection result
    :rtype: bool
    """
    check_port = addr.rfind(":")
    if check_port:
        addr_url = addr[:check_port]
        if not addr[check_port+1:].isdigit():
            return False
        addr_port = int(addr[check_port+1:])
    else:
        addr_url = addr
        addr_port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((addr_url, addr_port))
        s.close()
        return True
    except (ConnectionRefusedError, socket.gaierror):
        return False


def load_config_file(path: str):
    """Check config file content.

    :param path: file address
    :type path: str
    :return: Loading config file
    :rtype: str
    """
    try:
        return json.load(path)
    except json.JSONDecodeError:
        return ""


def validate_config_structure(config: dict):
    """Validate config content.

    :param config: config body
    :type config: dict
    :return: validation result in digit
    :rtype: int
    """
    # 'action' key/value validation
    if not config.get("actions"):
        return const.ACTION_KEY_NOT_FOUND
    if type(config["actions"]) is not list:
        return const.ACTION_VALUE_INVALID_TYPE
    if len(config["actions"]) == 0:
        return const.ACTION_VALUE_IS_EMPTY

    for item in config["actions"]:
        # 'command' key/value validation
        if item.get("command") is None:
            return const.COMMAND_KEY_NOT_FOUND
        if type(item["command"]) is str:
            return const.COMMAND_VALUE_INVALID_TYPE
        if len(item["command"]) == 0:
            return const.COMMAND_VALUE_IS_EMPTY

        # 'process' key/value validation
        if item.get("process") is None:
            return const.PROCESS_KEY_NOT_FOUND
        if type(item["process"]) is not int:
            return const.PROCESS_VALUE_INVALID_TYPE
        if item["process"] <= 0:
            return const.PROCESS_VALUE_INVALID_VALUE

        # 'thread' key/value validation
        if item.get("thread") is None:
            return const.THREAD_KEY_NOT_FOUND
        if type(item["thread"]) is not int:
            return const.THREAD_VALUE_INVALID_TYPE
        if item["thread"] <= 0:
            return const.THREAD_VALUE_INVALID_VALUE

        # 'io' key/value validation
        if item.get("io") is None:
            return const.IO_KEY_NOT_FOUND
        if type(item["io"]) is not list:
            return const.IO_VALUE_INVALID_TYPE
        if len(item["io"]) == 0:
            return const.IO_VALUE_INVALID_VALUE

    return True
