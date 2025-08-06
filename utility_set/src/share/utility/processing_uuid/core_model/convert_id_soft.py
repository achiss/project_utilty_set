"""
Processing ID (core): convert uuid
Methods:
    convert_id_soft
"""

from uuid import UUID
from typing import Tuple, Type, Any


def convert_id_soft(value: UUID | str,
                    reference_type: Type[Any]) -> Tuple[bool, UUID | str, str | None]:
    """
    Method: convert data - UUID / str (if the value has the same type, the data type conversion will be canceled)

    Args:
        value (UUID): converting data
        reference_type (type): reference data type

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
        if reference_type != type(value):
            return from_uuid_to_string(value, message=_message)

        return True, value, None

    elif check_data_type(value, as_uuid=False):
        if reference_type != type(value):
            return from_string_to_uuid(value, message=_message)

        return True, value, None

    else:
        _message: str = f'{_base_message}: {MESSAGE_TYPE_ERROR_ID.format('UUID or str', type(value).__name__)}'
        return False, _message, TypeError.__name__
