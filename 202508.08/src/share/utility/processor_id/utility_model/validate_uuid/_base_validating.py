"""
Script (processing id - validate uuid): validating data.
"""

from typing import Tuple

T: type[tuple] = Tuple[bool, bool | str, None | str]


def validate_uuid(value: str) -> T:
    """
    Base validation method (uuid).

    Returns:
        Tuple[bool, bool | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if validation (base) succeed - verification result (True or False), otherwise exception message;
            -   if validation (base) succeed - None, otherwise name string of exception type.
    """

    from data.pattern import REGEX_UUID
    from data.message import MSG_UNEXPECTED_ERROR

    try:
        _result: bool = bool(REGEX_UUID.match(string=value))
        return True, _result, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR
        return False, _message, type(e).__name__


def validate_uuid4_uuid5(value: str) -> T:
    """
    Base validation method (uuid4 and uuid5).

    Returns:
        Tuple[bool, bool | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if validation (base) succeed - verification result (True or False), otherwise exception message;
            -   if validation (base) succeed - None, otherwise name string of exception type.
    """

    from data.pattern import REGEX_UUID4, REGEX_UUID5
    from data.message import MSG_UNEXPECTED_ERROR

    try:
        _result: bool = bool(REGEX_UUID4.match(string=value)) or bool(REGEX_UUID5.match(string=value))
        return True, _result, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR
        return False, _message, type(e).__name__
