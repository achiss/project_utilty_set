"""
Script (processing id - convert uuid): converting data.
"""

from uuid import UUID
from typing import Tuple

from src.share.utility.processor_id.utility_model.convert_uuid._base_converting import base_converting
from src.share.utility.processor_id.utility_model.convert_uuid._verification_argument import \
    verification_argument_uuid_value, verification_argument_reference_type

T: type[tuple] = Tuple[bool, UUID | str, None | str]


def convert_uuid(value: UUID | str, reference_type: type) -> T:
    """
    Method (overload): converting - uuid to str / str to uuid

    Args:
         value (UUID | str): converting value data type
         reference_type (type): data type flag, if True - UUID else str.

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   If converting succeed: uuid number (UUID | str), otherwise exception message;
            -   if converting succeed - None, otherwise name string of exception type.
    """

    _flag, _data, _e = verification_argument_uuid_value(value)
    if not _flag:
        return False, _data, _e

    if not reference_type:
        return base_converting(value, is_type=_data)

    else:
        if not (_result := verification_argument_reference_type(reference_type))[0]:
            return _result

        if (reference_type == UUID and not _data) or (reference_type == str and _data):
            return base_converting(value, is_type=_data)

        return True, value, None
