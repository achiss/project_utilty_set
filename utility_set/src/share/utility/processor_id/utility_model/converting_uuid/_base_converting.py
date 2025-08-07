"""
Script (processing id - convert uuid): converting data.
"""

from uuid import UUID
from typing import Tuple

T: type[tuple] = Tuple[bool, UUID | str, None | str]


def base_converting(value: UUID | str,
                    is_type: bool) -> T:
    """
    Method: base converting value (from converting uuid). From uuid to str or from str to uuid.

    Args:
         value (UUID | str): converting value data type
         is_type (bool): data type flag, if True - UUID else str.

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   Successes (True) operation, otherwise False.
            -   `If operation succeed`: uuid number or uuid string. `If operation failed`: exception message.
            -   `If operation succeed`: None. `If operation failed`: name of exception type.
    """

    from data.message import MSG_UNEXPECTED_ERROR

    try:
        if is_type:
            _result: str = value.__str__()

        _result: UUID = UUID(value)
        return True, _result, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR.format(':', e)
        return False, _message, type(e).__name__
