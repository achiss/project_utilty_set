from typing import TypeAlias, Tuple, Type
from uuid import UUID
from uuid import uuid5

T: TypeAlias = Tuple[bool, UUID | str, Type[Exception] | None]


def generate_uuid5(object_data: str, object_domain: UUID) -> 'T':

    from data.message import MESSAGE_UNEXPECTED_ERROR

    _func_message: str = 'uuid5 generation'

    try:
        _result  = uuid5(namespace=object_domain, name=object_data)
        return True, _result, None

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, e)
        return False, _message, type(e)
