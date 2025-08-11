"""
Processing ID (core): generate uuid
Methods:
    generate_id
"""

from uuid import UUID
from typing import Tuple, Any
from typing import overload

from src.share.utility.processing_uuid.core_model.generate_uuid import (
    generate_uuid4, generate_uuid5, arguments_processing_name_string)

from data import MASSAGE_BASE_GENERATE, MESSAGE_TYPE_ERROR, MESSAGE_UNEXPECTED_ERROR


_message_data_type_error: str = f'{MASSAGE_BASE_GENERATE} - {MESSAGE_TYPE_ERROR} (from attribute "domain")'
_message_unexpected_error: str = f'{MASSAGE_BASE_GENERATE} - {MESSAGE_UNEXPECTED_ERROR}'
_message_value_error: str = f'{MASSAGE_BASE_GENERATE}: incorrect args (object_string) length, should be defined'


@overload
def generate_id() -> Tuple[bool, UUID | str, None | str]: ...


@overload
def generate_id(*object_string: Any,
                domain: UUID) -> Tuple[bool, UUID | str, None | str]: ...


def generate_id(*object_string: Any,
                domain: UUID = None) -> Tuple[bool, UUID | str, None | str]:
    """
    Method (overload): generate uuid (uuid4 or uuid5)

    Args:
        object_string (Any): list of object data (used in uuid5)
        domain (UUID): initial uuid (used in uuid5)

    Returns:
        Tuple[bool, UUID | str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid value (uuid4 or uuid5) if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    if not domain:
        return generate_uuid4(msg_unexpected_error=_message_unexpected_error)

    if len(object_string) == 0:
        return False, _message_value_error, ValueError.__name__

    else:
        if not (_result := arguments_processing_name_string(
                object_string, msg_unexpected_error=_message_unexpected_error))[0]:
            return _result

        object_string: str = _result[1]

    if not isinstance(domain, UUID):
        _message: str = _message_data_type_error.format('UUID', type(domain).__name__)
        return False, _message, TypeError.__name__

    return generate_uuid5(domain=domain, object_string=object_string, msg_unexpected_error=_message_unexpected_error)
