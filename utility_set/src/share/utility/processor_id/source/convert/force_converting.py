from typing import TypeAlias, Type, Tuple
from uuid import UUID


T: TypeAlias = str | UUID | Tuple[str, Type[Exception]]


def force_converting(value: str | UUID,
                     value_type: bool,
                     base_message: str,
                     message_unexpected: str) -> T:

    try:
        return str(value) if value_type else UUID(value)

    except Exception as e:
        _message: str = message_unexpected.format(base_message, e)
        return _message, type(e)
