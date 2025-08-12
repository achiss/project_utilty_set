from typing import TypeAlias, Tuple, Type, Any

from data.settings import PASS_MIN_LENGTH, PASS_MAX_LENGTH


T: TypeAlias = None | Tuple[str, Type[Exception]]

BASE_MESSAGE: str = 'validate password string'


def validate_password_string(value: Any,
                             message_type: str, message_value: str, message_unexpected: str) -> T:

    try:
        if isinstance(value, bytes):
            if PASS_MIN_LENGTH < len(value) < PASS_MAX_LENGTH:
                return None

            _message: str = message_value.format(
                BASE_MESSAGE, f'should be between {PASS_MIN_LENGTH} and {PASS_MAX_LENGTH}')
            return _message, ValueError

        else:
            _message: str = message_type.format(BASE_MESSAGE, 'str', type(value).__name__)
            return _message, TypeError

    except Exception as e:
        _message: str = message_unexpected.format(BASE_MESSAGE, e)
        return _message, type(e)
