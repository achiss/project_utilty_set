"""
Processing ID (core): convert uuid
Methods:
    convert_id_force
"""

from uuid import UUID
from typing import Tuple


def convert_id_force(value: UUID | str) -> Tuple[bool, UUID | str, str | None]:
    """
    Method: convert data - UUID / str (both ways)

    Args:
        value (UUID): converting data

    Returns:
        Tuple[bool, UUID | str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid in string data type if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    from data import MESSAGE_TYPE_ERROR_ID, MESSAGE_UNEXPECTED_ERROR_ID
    from src.share.utility.processing_uuid.core_model.check_data_type import check_data_type
    from src.share.utility.processing_uuid.core_model.convert_uuid_method import from_string_to_uuid, from_uuid_to_string

    _base_message: str = 'Failed ID conversion'
    _message: str = f'{_base_message}: {MESSAGE_UNEXPECTED_ERROR_ID}'

    if check_data_type(value, as_string=False):
        return from_uuid_to_string(value, _message)

    elif check_data_type(value, as_uuid=False):
        return from_string_to_uuid(value, _message)

    else:
        _message: str = f'{_base_message}: {MESSAGE_TYPE_ERROR_ID.format('UUID or str', type(value).__name__)}'
        return False, _message, TypeError.__name__
