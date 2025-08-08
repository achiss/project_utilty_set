"""
Script (processing id - convert uuid): converting data.
"""

from uuid import UUID
from typing import Tuple

T: type[tuple] = Tuple[bool, UUID | str, None | str]


def base_converting(value: UUID | str,
                    is_type: bool) -> T:
    """
    Base converting (from converting uuid) method, from uuid to str or from str to uuid.

    Args:
         value (UUID | str): converting value data type
         is_type (bool): data type flag, if True - UUID else str.

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   If converting (base) succeed: uuid number (UUID | str), otherwise exception message;
            -   if converting (base) succeed - None, otherwise name string of exception type.
    """

    from data.message import MSG_UNEXPECTED_ERROR

    try:
        if is_type:
            _result: str = value.__str__()

        else:
            _result: UUID = UUID(value)

        return True, _result, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR.format('-', e)
        return False, _message, type(e).__name__
