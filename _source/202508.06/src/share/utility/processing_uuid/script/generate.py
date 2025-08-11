from uuid import uuid4, uuid5
from uuid import UUID
from typing import overload
from typing import Tuple, Type


def get_uuid4(message: str) -> Tuple[bool, UUID | str, Type[Exception] | None]:

    try:
        return True, uuid4(), None

    except Exception as e:
        _msg: str = message.format(':', e)
        return False, _msg, type(e)


def get_uuid5(uuid_value: UUID, string_value: str, message: str) -> Tuple[bool, UUID | str, Type[Exception] | None]:

    try:
        return True, uuid5(namespace=uuid_value, name=string_value), None

    except Exception as e:
        _msg: str = message.format(':', e)
        return False, _msg, type(e)


@overload
def generate() -> Tuple[bool, UUID | str, Type[Exception] | None]: ...


@overload
def generate(object_value: str, domain: UUID) -> Tuple[bool, UUID | str, Type[Exception] | None]: ...


def generate(object_value: str = None, domain: UUID = None) -> Tuple[bool, UUID | str, Type[Exception] | None]:

    from data import MSG_UNEXPECTED_ERROR

    if not (object_value or domain):
        return get_uuid4(MSG_UNEXPECTED_ERROR)

    elif object_value and domain:
        return get_uuid5(domain, object_value, MSG_UNEXPECTED_ERROR)

    else:
        _msg: str = object_value.format('', '').strip()
        return False, _msg, Exception
