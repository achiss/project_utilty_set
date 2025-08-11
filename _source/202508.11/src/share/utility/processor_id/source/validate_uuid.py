from typing import TypeAlias, Tuple, Type
from typing import overload
from uuid import UUID

from src.share.utility.processor_id.source.common_method.verify_attribute import verify_uuid_value
from src.share.utility.processor_id.source.validate_uuid_method.processing_not_common_check import processing_not_common_check

T: TypeAlias = Tuple[bool, bool | str, Type[Exception] | None]


@overload
def validate_uuid(value: UUID | str) -> 'T': ...


@overload
def validate_uuid(value: UUID | str, is_common: bool) -> 'T': ...


def validate_uuid(value: UUID | str = None, is_common: bool = None) -> 'T':
    """
    Convert UUID (overload) method: str - UUID | UUID - str
        1-st: force convert - mandatory data type conversion;
        2-nd: soft convert - conversion when the reference value does not match.

    Args:
        value (UUID | str): processed value;
        is_common (bool): .

    Returns:
        -   (Tuple[str, UUID | str, Type[Exception] | None])
        -   If operation succeeded - True, False otherwise.
        -   if operation succeeded return True or False depends on verification method, else return exception message.
        -   If operation succeeded return None, else return exception type.
    """

    _flag, _data, _e = verify_uuid_value(value)
    if not _flag and _e == ValueError:
        return True, False, None

    elif not _flag:
        return False, _data, _e

    if not (is_common or _data):
        return True, True, None

    else:
        if is_common:
            _flag, _data, _e = processing_not_common_check(value)
            if not _flag and _e == ValueError:
                return True, False, None

            elif not _flag:
                return False, _data, _e

        return True, True, None
