from typing import TypeAlias, Tuple, Type
from uuid import UUID
from uuid import uuid4

T: TypeAlias = Tuple[bool, UUID | str, Type[Exception] | None]


def generate_uuid4() -> 'T':

    from data.message import MESSAGE_UNEXPECTED_ERROR

    _func_message: str = 'uuid5 generation'

    try:
        _result  = uuid4()
        return True, _result, None

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, e)
        return False, _message, type(e)
