"""
Script (processing id - convert uuid): converting data.
"""

from uuid import UUID
from typing import Tuple, Type
from typing import overload

from src.share.utility.processor_id.utility_model.converting_uuid._base_converting import base_converting
from src.share.utility.processor_id.utility_model.converting_uuid._verification_argument import \
    verification_argument_uuid_value, verification_argument_reference_type

T: type[tuple] = Tuple[bool, UUID | str, None | str]


@overload
def converting_uuid(value: UUID | str) -> T: ...


@overload
def converting_uuid(value: UUID | str, reference_type: type) -> T: ...


def converting_uuid(value: UUID | str, reference_type: type = None) -> T:
    """
    Method (overload): converting - uuid to str / str to uuid

    Args:
         value (UUID | str): converting value data type
         reference_type (type): data type flag, if True - UUID else str.

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   Successes (True) operation, otherwise False.
            -   `If operation succeed`: uuid number or uuid string. `If operation failed`: exception message.
            -   `If operation succeed`: None. `If operation failed`: name of exception type.
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
