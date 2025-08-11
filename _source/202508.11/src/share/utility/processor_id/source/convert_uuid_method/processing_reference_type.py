from typing import TypeAlias, Tuple, Type
from uuid import UUID

T: TypeAlias = Tuple[bool, bool | str, Type[Exception] | None]


def processing_reference_type(value: type) -> T:

    from data.message import MESSAGE_TYPE_ERROR

    _func_message: str = 'parameter "reference type" for soft converting method'

    if isinstance(value, UUID):
        return True, True, None

    elif isinstance(value, str):
        return True, False, None

    else:
        _message: str = MESSAGE_TYPE_ERROR.format(_func_message, 'UUID or str', type(value).__name__)
        return False, _message, TypeError
