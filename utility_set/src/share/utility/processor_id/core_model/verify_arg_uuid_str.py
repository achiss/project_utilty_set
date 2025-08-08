from typing import Tuple, Type, Any
from uuid import UUID


T: type[tuple] = Tuple[bool, bool | str, Type[Exception] | None]


def verify_arg_uuid_str(value: Any) -> T:
    """
    Verify argument (UUID or str) data type.

    Returns: Tuple[bool, bool | str, Type[Exception | None]]
        1   -   successful operation. True if success, False otherwise.\n
        2   -   verification result. True if UUID data type, False str. If operation failed exception message.\n
        3   -   exception type if operation failed, None otherwise.
    """

    from data.conf import REGEX_UUID
    from data.message import MESSAGE_VALUE_ERROR, MESSAGE_TYPE_ERROR

    if isinstance(value, str):
        if len(value) != 32 or len(value) != 36:
            _message: str = MESSAGE_TYPE_ERROR.format(
                'verify uuid value', f'expected 32 or 36 chars, got {len(value)}').strip()
            return False, _message, ValueError

        if not REGEX_UUID.match(value):
            _message: str = MESSAGE_VALUE_ERROR.format(
                'verify uuid value', 'does not match the specified format').strip()
            return False, _message, ValueError

        return True, False, None

    elif isinstance(value, UUID):
        return True, True, None

    _message: str = MESSAGE_TYPE_ERROR.format(
        'verify uuid value', 'UUID or str', type(value).__name__)
    return False, _message, TypeError
