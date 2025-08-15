from typing import TypeAlias, Type, Tuple, Any, Callable
from uuid import UUID


T: TypeAlias = UUID | Tuple[str, Type[Exception]]


def generate_uuid(*object_data: Any,
                  object_domain: UUID | None,
                  message_type: str,
                  message_unexpected: str,
                  generate_uuid4: Callable,
                  generate_uuid5: Callable,
                  processing_object_data: Callable) -> T:

    _base_message: str = 'Generate UUID failed'

    if object_domain is None:
        return generate_uuid4(base_message=_base_message, message_unexpected=message_unexpected)

    else:
        object_data: str | Tuple[str, Type[Exception]] = processing_object_data(
            *object_data, base_message=_base_message, message_unexpected=message_unexpected,)
        if str != type(object_data):
            return object_data

        if not isinstance(object_domain, UUID):
            _message: str = message_type.format(_base_message, 'UUID', type(object_domain).__name__)
            return _message, TypeError

        return generate_uuid5(
            object_data, object_domain, base_message=_base_message, message_unexpected=message_unexpected)
