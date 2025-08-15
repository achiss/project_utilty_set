from typing import TypeAlias, Type, Tuple
from uuid import UUID


T: TypeAlias = str | UUID | Tuple[str, Type[Exception]]


def soft_converting(value: str | UUID,
                    reference_type: type,
                    value_type: bool,
                    base_message: str,
                    message_unexpected: str) -> T:

    try:
        if value_type:
            return value if reference_type == UUID else str(value)

        else:
            return value if reference_type == str else UUID(value)

    except Exception as e:
        _message: str = message_unexpected.format(base_message, e)
        return _message, type(e)
