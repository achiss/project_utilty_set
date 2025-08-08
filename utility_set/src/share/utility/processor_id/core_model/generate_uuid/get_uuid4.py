from typing import Tuple, Type
from uuid import UUID
from uuid import uuid4


T: type[tuple] = Tuple[bool, UUID | str, Type[Exception] | None]


def get_uuid4() -> T:
    """
    Generate uuid value (uuid4).

    Returns: Tuple[bool, UUID | str, Type[Exception | None]]
        1   -   successful operation. True if success, False otherwise.\n
        2   -   generation result. If operation succeed UUID value. If operation failed exception message.\n
        3   -   exception type if operation failed, None otherwise.
    """

    from data.message import MESSAGE_UNEXPECTED_ERROR

    try:
        _result: UUID = uuid4()
        return True, _result, None

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format('generating uuid4', e)
        return False, _message, type(e)
