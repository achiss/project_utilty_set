"""
Script (processing id - generate uuid): generating data.
"""

from uuid import UUID
from uuid import uuid4, uuid5
from typing import Tuple

T: type[tuple] = Tuple[bool, UUID | str, None | str]


def  base_generating(object_data: str | None,
                     object_domain: UUID | None) -> T:
    """
    Base generating method.

    Args:
        object_data (str | None): (used for generate uuid5)
        object_domain (UUID | None): (used for generate uuid5)

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if generation (base) succeed - uuid number, otherwise exception message;
            -   if generation (base) succeed - None, otherwise name string of exception type.
    """

    from data.message import MSG_UNEXPECTED_ERROR

    try:
        if (object_data and object_domain) is None:
            _result: UUID = uuid4()

        else:
            _result: UUID = uuid5(namespace=object_domain, name=object_data)

        return True, _result, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR.format('-', e)
        return False, _message, type(e).__name__
