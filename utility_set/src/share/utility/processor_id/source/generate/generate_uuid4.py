from typing import TypeAlias, Type, Tuple
from uuid import UUID
from uuid import uuid4


T: TypeAlias = UUID | Tuple[str, Type[Exception]]


def generate_uuid4(base_message: str,
                   message_unexpected: str) -> T:

    base_message = f'{base_message} (operation uuid4)'

    try:
        _result: UUID = uuid4()
        return _result

    except Exception as e:
        _message: str = message_unexpected.format(base_message, e)
        return _message, type(e)
