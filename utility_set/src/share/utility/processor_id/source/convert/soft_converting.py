from typing import TypeAlias, Type, Tuple
from uuid import UUID


S: TypeAlias = str | UUID
T: TypeAlias = S | Tuple[str, Type[Exception]]


def soft_converting(value: S,
                    value_type: bool,
                    reference_type: type,
                    base_message: str,
                    message_unexpected: str) -> T:

    _method_name: str = '(method: soft converting)'

    try:
        if value_type:
            return value if reference_type == UUID else str(value)

        return value if reference_type == str else UUID(value)

    except Exception as e:
        _message: str = message_unexpected.format(
            f'{base_message} {_method_name}', e)
        return _message, type(e)
