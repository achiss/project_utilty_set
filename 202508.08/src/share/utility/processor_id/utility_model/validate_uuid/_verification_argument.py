"""
Script (processing id - validate uuid): verification argument data.
"""

from typing import Tuple, Any
from uuid import UUID

T: type[tuple] = Tuple[bool, bool | str, None | str]


def verification_argument_uuid_value(value: Any) -> T:
    """
    """

    from data.message import MSG_DATA_TYPE_ERROR, MSG_VALUE_ERROR

    if isinstance(value, UUID):
        return True, True, None

    elif isinstance(value, str):
        if len(value) != 32 or len(value) != 64:
            _message: str = MSG_VALUE_ERROR
            return False, _message, ValueError.__name__

        return True, False, None

    else:
        _message: str = MSG_DATA_TYPE_ERROR
        return False, _message, TypeError.__name__
