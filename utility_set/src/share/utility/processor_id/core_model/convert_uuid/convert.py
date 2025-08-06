"""
Utility method: converting uuid string (from UUID to str, from str to UUID)
"""

from uuid import UUID
from typing import Tuple, Type
from typing import overload

from src.share.utility.processor_id.core_model.convert_uuid._validate_uuid import validate_uuid
from src.share.utility.processor_id.core_model.convert_uuid._from_str_to_uuid import from_str_to_uuid
from src.share.utility.processor_id.core_model.convert_uuid._from_uuid_to_str import from_uuid_to_str


@overload
def convert(value: UUID | str) -> Tuple[bool, UUID | str, None | str]: ...


@overload
def convert(value: UUID | str,
            reference_type: Type[UUID, str]) -> Tuple[bool, UUID | str, None | str]: ...


def convert(value: UUID | str,
            reference_type: Type[UUID, str] = None) -> Tuple[bool, UUID | str, None | str]:

    try:
        _flag, _data, _e = validate_uuid(value)
        if not _flag:
            return False, _data, _e

        if not reference_type:
            if not _data:
                return from_str_to_uuid(value)

            return from_uuid_to_str(value)

        else:
            if not _data and reference_type is str:
                return True, value, None

            elif not _data and reference_type is UUID:
                return from_uuid_to_str(value)

            elif _data and reference_type is str:
                return True, value, None

            elif _data and reference_type is UUID:
                return from_uuid_to_str(value)

    except Exception as e:
        _message: str = ''
        return False, _message, type(e).__name__
