from typing import TypeAlias, Type, Tuple
from uuid import UUID


S: TypeAlias = str | UUID
T: TypeAlias = S | Tuple[str, Type[Exception]]


def force_converting(value: S,
                     value_type: bool,
                     base_message: str,
                     message_unexpected: str) -> T:

    _method_name: str = '(method: force converting)'

    try:
        return str(value) if value_type else UUID(value)

    except Exception as e:
        _message: str = message_unexpected.format(
            f'{base_message} {_method_name}', e)
        return _message, type(e)
