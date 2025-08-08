"""
Script (processing id - generate uuid): verification argument data.
"""

from typing import Tuple, Any
from uuid import UUID

T: type[tuple] = Tuple[bool, None | str, None | str]


def verification_argument_object_data(*args: Any) -> T:
    """
    Verification object data method.

    Args:
        args (Any): verification data value(s).

    Returns:
        Tuple[bool, None | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if verification succeed - None, otherwise exception message;
            -   if verification succeed - None, otherwise name string of exception type.
    """

    from data.message import  MSG_ATTRIBUTE_ERROR, MSG_VALUE_ERROR

    if args is None:
        _message: str = MSG_ATTRIBUTE_ERROR.format('parameter (object data) in generating uuid should be defined')
        return False, _message, AttributeError.__name__

    if len(args) == 0:
        _message: str = MSG_VALUE_ERROR.format('parameter (object data) in generating cannot be empty')
        return False, _message, ValueError.__name__

    return True, None, None


def verification_argument_object_domain(value: UUID) -> T:
    """
    Verification object domain method.

    Args:
        value (UUID): verification domain value.

    Returns:
        Tuple[bool, None | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if verification succeed - None, otherwise exception message;
            -   if verification succeed - None, otherwise name string of exception type.
    """

    from data.message import MSG_DATA_TYPE_ERROR

    if not isinstance(value, UUID):
        _message: str = MSG_DATA_TYPE_ERROR.format('UUID', type(value).__name__)
        return False, _message, TypeError.__name__

    return True, None, None
