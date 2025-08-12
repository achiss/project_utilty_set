from typing import TypeAlias, Tuple, Type, Callable

from bcrypt import checkpw


T: TypeAlias = bool | Tuple[str, Type[Exception]]

BASE_MESSAGE: str = 'validate password'


def validate_hash(value: str, reference_value: bytes,
                  message_type: str, message_value: str, message_unexpected: str,
                  check_password_string: Callable, check_hashed_password: Callable) -> T:

    if _checked_value := check_password_string(value, message_type, message_value, message_unexpected) is not None:
        return _checked_value

    if _checked_value := check_hashed_password(reference_value, message_type, message_value, message_unexpected) is not None:
        return _checked_value

    try:
        value: bytes = value.encode(encoding='utf-8')
        return checkpw(password=value, hashed_password=reference_value)

    except Exception as e:
        _message: str = message_unexpected.format()
        return _message, type(e)
