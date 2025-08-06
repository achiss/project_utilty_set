"""
Processing ID (core): verification (common)
Methods:
    check_data_type
"""

from uuid import UUID
from typing import Tuple


def check_data_type(value: UUID | str,
                    as_string: bool = True,
                    as_uuid: bool = True) -> Tuple[bool, bool | str, None | str]:
    """
    Method: checking the uuid number by UUID or str data type

    Args:
        value (UUID): checked value
        as_string (bool): verify data type as str (default: True)
        as_uuid (bool): verify data type as UUID (default: True)

    Returns:
        bool: True if succeeded, False otherwise
    """

    from data import MESSAGE_TYPE_ERROR_ID

    _result: bool = False
    if as_string and as_uuid:
        _result = isinstance(value, (UUID, str))

    elif as_string and not as_uuid:
        _result = isinstance(value, str)

    elif not as_string and as_uuid:
        _result = isinstance(value, UUID)

    else:
        _message: str = MESSAGE_TYPE_ERROR_ID.format('UUID or str', f'{type(value).__name__}')
        return False, _message, TypeError.__name__

    return True, _result, None
