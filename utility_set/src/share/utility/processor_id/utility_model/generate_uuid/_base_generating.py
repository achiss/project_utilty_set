"""
Script (processing id - generate uuid): generating data.
"""

from uuid import UUID
from uuid import uuid4, uuid5
from typing import Tuple

T: type[tuple] = Tuple[bool, UUID | str, None | str]


def generate_uuid4() -> T:
    """
    Base generating method (uuid4).

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if generation (base) succeed - uuid number, otherwise exception message;
            -   if generation (base) succeed - None, otherwise name string of exception type.
    """

    from data.message import MSG_UNEXPECTED_ERROR

    try:
        _result: UUID = uuid4()
        return True, _result, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR.format('- during generating uuid 4 -', e)
        return False, _message, type(e).__name__


def generate_uuid5(object_data: str, object_domain: UUID) -> T:
    """
    Base generating method (uuid5).

    Args:
        object_data (str | None): object data string (parameter `name`)
        object_domain (UUID | None): object domain (parameter `namespace`)

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if generation (base) succeed - uuid number, otherwise exception message;
            -   if generation (base) succeed - None, otherwise name string of exception type.
    """

    from data.message import MSG_UNEXPECTED_ERROR

    try:
        _result: UUID = uuid5(namespace=object_domain, name=object_data)
        return True, _result, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR.format('- during generating uuid 5 -', e)
        return False, _message, type(e).__name__
