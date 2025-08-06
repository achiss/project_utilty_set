"""
Processing ID (core): validate id
Methods:
    check_string_uuid_common
    check_string_uuid
"""

from typing import Tuple
from re import Pattern


def check_string_uuid_common(value: str,
                             regex: Pattern,
                             message: str) -> Tuple[bool, bool | str, None | str]:
    """
    Method: checking the string for the fact that it is a UUID (used common pattern)

    Args:
        value (UUID): data type value
        regex (Pattern): common UUID regex template
        message (str): exception message

    Returns:
        Tuple[bool, bool | str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid in string data type if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    try:
        _result: bool = bool(regex.fullmatch(string=value))
        return True, _result, None

    except Exception as e:
        _message: str = message.format(':', e)
        return False, _message, type(e).__name__


def check_string_uuid(value: str,
                      regex_uuid4: Pattern,
                      regex_uuid5: Pattern,
                      message: str) -> Tuple[bool, bool | str, None | str]:
    """
    Method: checking the string for the fact that it is a UUID (used uuid4 and uuid5 patterns)

    Args:
        value (UUID): data type value
        regex_uuid4 (Pattern): uuid4 regex template
        regex_uuid5 (Pattern): uuid5 regex template
        message (str): exception message

    Returns:
        Tuple[bool, bool | str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid in string data type if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """


    try:
        _result: bool = bool(regex_uuid4.fullmatch(string=value)) or bool(regex_uuid5.fullmatch(string=value))
        return True, _result, None

    except Exception as e:
        _message: str = message.format(':', e)
        return False, _message, type(e).__name__
