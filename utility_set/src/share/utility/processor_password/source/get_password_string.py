from typing import TypeAlias, Type, Tuple, List

from secrets import SystemRandom
from secrets import choice
from string import ascii_lowercase, ascii_uppercase


T: TypeAlias = str | Tuple[str, Type[Exception]]


def get_password_string(length_value: int,
                        password_parts: List[str],
                        base_message: str,
                        message_exception: str) -> T:

    try:
        _chars_length: int = length_value - len(password_parts)
        _upper_count: int = max(1, int(_chars_length * 0.3))
        _lower_count: int = _chars_length - _upper_count

        _upper_chars: List[str] = [choice(ascii_uppercase) for _ in range(_upper_count)]
        _lower_chars: List[str] = [choice(ascii_lowercase) for _ in range(_lower_count)]

        _password: List[str] = password_parts + _upper_chars + _lower_chars
        SystemRandom().shuffle(_password)

        return ''.join(_password)

    except Exception as e:
        _message: str = message_exception.format(base_message, e)
        return _message, type(e)
