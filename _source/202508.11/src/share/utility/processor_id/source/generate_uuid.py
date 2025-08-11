from typing import TypeAlias, Tuple, Type, Any
from typing import overload
from uuid import UUID

from src.share.utility.processor_id.source.generate_uuid_method.generate_uuid4 import generate_uuid4
from src.share.utility.processor_id.source.generate_uuid_method.generate_uuid5 import generate_uuid5
from src.share.utility.processor_id.source.generate_uuid_method.processing_object_data import processing_object_data
from src.share.utility.processor_id.source.common_method.verify_attribute import verify_uuid_value

T: TypeAlias = Tuple[bool, UUID | str, Type[Exception] | None]


@overload
def generate_uuid() -> 'T': ...


@overload
def generate_uuid(*object_data: Any, object_domain: UUID) -> 'T': ...


def generate_uuid(*object_data: Any, object_domain: UUID = None) -> 'T':
    """
    Generate UUID (overload) method:
        1-st: generate uuid4
        2-nd: generate uuid5

    Args:
        object_data (Any): object data (for uuid5)
        object_domain (UUID): object domain (for uuid5)

    Returns:
        -   (Tuple[str, UUID | str, Type[Exception] | None])
        -   If operation succeeded - True, False otherwise.
        -   if operation succeeded return UUID, else return exception message.
        -   If operation succeeded return None, else return exception type.
    """

    if object_domain is None or len(object_data) == 0:
        return generate_uuid4()

    else:
        if (_result := verify_uuid_value(object_domain))[0]:
            return _result

        _flag, _data, _e = processing_object_data(object_data)
        if not _flag:
            return False, _data, _e

        return generate_uuid5(object_data=_data, object_domain=object_domain)
