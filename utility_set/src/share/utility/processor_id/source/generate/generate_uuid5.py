from typing import TypeAlias, Type, Tuple, Callable
from uuid import UUID
from uuid import uuid5


T: TypeAlias = UUID | Tuple[str, Type[Exception]]


def generate_uuid5(object_data: str,
                   object_domain: UUID,
                   base_message: str,
                   message_unexpected: str) -> T:

    base_message = f'{base_message} (operation uuid5)'

    try:
        _result: UUID = uuid5(name=object_data, namespace=object_domain)
        return _result

    except Exception as e:
        _message: str = message_unexpected.format(base_message, e)
        return _message, type(e)
