"""
Processing ID (core): generate uuid
Methods:
    generate_id
"""

from uuid import UUID
from typing import Tuple, Any
from typing import overload


@overload
def generate_id() -> Tuple[bool, UUID | str, None | str]: ...


@overload
def generate_id(*name_args: Any,
                domain: UUID) -> Tuple[bool, UUID | str, None | str]: ...


def generate_id(*name_args: Any,
                domain: UUID = None) -> Tuple[bool, UUID | str, None | str]:

    from src.share.utility.processing_uuid.core_model.check_data_type import check_data_type
    from src.share.utility.processing_uuid.core_model.generate_uuid_args import args_processing
    from src.share.utility.processing_uuid.core_model.generate_uuid_method import generate_uuid4, generate_uuid5

    from data import MASSAGE_BASE_GENERATE_ID, MESSAGE_TYPE_ERROR_ID, MESSAGE_UNEXPECTED_ERROR_ID

    _message_data_type: str = f'{MASSAGE_BASE_GENERATE_ID} - {MESSAGE_TYPE_ERROR_ID}'
    _message_unexpected: str = f'{MASSAGE_BASE_GENERATE_ID} - {MESSAGE_UNEXPECTED_ERROR_ID}'

    if not domain:
        return generate_uuid4(message=_message_unexpected)

    if not (_result := args_processing(name_args, message=_message_unexpected))[0]:
        return _result

    name_string: str = _result[1]

    if not check_data_type(domain, as_string=False):
        _message: str = _message_data_type.format('UUID', type(domain).__name__)
        return False, _message, TypeError.__name__

    return generate_uuid5(domain=domain, name_string=name_string, message=_message_unexpected)
