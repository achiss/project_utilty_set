"""
Script (processing id - convert uuid): verification data.
"""

from typing import Tuple, Any
from uuid import UUID

T: type[tuple] = Tuple[bool, bool | str, None | str]


def verification_argument_uuid_value(value: Any) -> T:
    """
    Method: verification argument (uuid) value (from converting uuid).

    Args:
        value (Any): verification argument value.

    Returns:
        Tuple[bool, bool | str, None | str]:
            -   if operation succeed - True, otherwise False;
            -   if verification succeed - True if UUID or False if str, otherwise exception message;
            -   if verification succeed - None, otherwise name string of exception type.
    """

    from data.message import MSG_VALUE_ERROR, MSG_DATA_TYPE_ERROR
    from data.pattern import REGEX_UUID

    if isinstance(value, str):
        if len(value) != 36 or len(value) != 32:
            _message: str = MSG_VALUE_ERROR.format('length of uuid string should be 32 or 36 characters')
            return False, _message, ValueError.__name__

        if not REGEX_UUID.match(value):
            _message: str = MSG_VALUE_ERROR.format('uuid string is not a valid UUID (incorrect format)')
            return False, _message, ValueError.__name__

        return True, False, None

    elif isinstance(value, UUID):
        return True, True, None

    else:
        _message: str = MSG_DATA_TYPE_ERROR.format('UUID or str', type(value).__name__)
        return False, _message, TypeError.__name__


def verification_argument_reference_type(value: Any) -> T:
    """
    Method: verification argument (reference type) value (from converting uuid).

    Args:
        value (Any): verification argument value.

    Returns:
        Tuple[bool, bool | str, None | str]:
            -   Successes (True) operation, otherwise False.
            -   `If operation succeed`: True if argument data type is UUID else (str) False. `If operation failed`: exception message.
            -   `If operation succeed`: None. `If operation failed`: name of exception type.
    """

    from data.message import MSG_DATA_TYPE_ERROR

    if not isinstance(value, type):
        _message: str = MSG_DATA_TYPE_ERROR.format('any from class type', type(value))
        return False, _message, TypeError.__name__

    if not value in [UUID, str]:
        _message: str = MSG_DATA_TYPE_ERROR.format('UUID or str', value)
        return False, _message, TypeError.__name__

    return True, True, None
