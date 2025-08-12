from typing import TypeAlias, Tuple, Type, Callable

from bcrypt import gensalt, hashpw


T: TypeAlias = bytes | Tuple[str, Type[Exception]]

BASE_MESSAGE: str = 'generate password hash'


def generate_hash(value: str,
                  message_type: str, message_value: str, message_unexpected: str,
                  check_password_string: Callable,
                  iteration_number: int, prefix_string: bytes) -> T:

    if _checked_value := check_password_string(value, message_type, message_value, message_unexpected) is not None:
        return _checked_value

    try:
        _salt: bytes = gensalt(rounds=iteration_number, prefix=prefix_string)
        value: bytes = value.encode(encoding='utf-8')
        return hashpw(password=value, salt=_salt)

    except Exception as e:
        _message: str = message_unexpected.format(BASE_MESSAGE, e)
        return _message, type(e)
