from typing import TypeAlias, Tuple, Type
from typing import overload
from uuid import UUID

from src.share.utility.processor_id.source.common_method.verify_attribute import verify_uuid_value
from src.share.utility.processor_id.source.convert_uuid_method.convert_force import convert_force
from src.share.utility.processor_id.source.convert_uuid_method.convert_soft import convert_soft
from src.share.utility.processor_id.source.convert_uuid_method.processing_reference_type import processing_reference_type

T: TypeAlias = Tuple[bool, UUID | str, Type[Exception] | None]


@overload
def convert_uuid(value: UUID | str) -> 'T': ...


@overload
def convert_uuid(value: UUID | str, reference_type: type) -> 'T': ...


def convert_uuid(value: UUID | str = None, reference_type: type = None) -> 'T':
    """
    Convert UUID (overload) method: str - UUID | UUID - str
        1-st: force convert - mandatory data type conversion;
        2-nd: soft convert - conversion when the reference value does not match.

    Args:
        value (UUID | str): processed value;
        reference_type (type): the reference data type (for soft conversion).

    Returns:
        -   (Tuple[str, UUID | str, Type[Exception] | None])
        -   If operation succeeded - True, False otherwise.
        -   if operation succeeded return UUID | str, else return exception message.
        -   If operation succeeded return None, else return exception type.
    """

    _flag, _data, _e = verify_uuid_value(value)
    if not _flag:
        return False, _data, _e

    if not reference_type:
        return convert_force(value, value_type=_data)

    else:
        if not (_result := processing_reference_type(reference_type))[0]:
            return _result

        return convert_soft(value, value_type=_data, reference_type=_result[1])
