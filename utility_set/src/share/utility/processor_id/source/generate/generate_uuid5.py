from typing import TypeAlias, Type, Tuple, Callable
from uuid import UUID
from uuid import uuid5


T: TypeAlias = UUID | Tuple[str, Type[Exception]]


def generate_uuid5(object_string: str,
                   object_domain: UUID,
                   base_message: str,
                   message_unexpected: str,
                   check_object_string: Callable,
                   check_object_domain: Callable) -> T:

    _checked_object_string: None | Tuple[str, Type[Exception]] = check_object_string(object_string)
    if None != _checked_object_string:
        return _checked_object_string

    _checked_object_domain: None | Tuple[str, Type[Exception]] = check_object_domain(object_domain)
    if None != _checked_object_domain:
        return _checked_object_domain

    try:
        _result: UUID = uuid5(name=object_string, namespace=object_domain)
        return _result

    except Exception as e:
        _message: str = message_unexpected.format(base_message, e)
        return _message, type(e)
