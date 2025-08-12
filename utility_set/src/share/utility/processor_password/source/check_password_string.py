from typing import TypeAlias, Type, Tuple, Any


T: TypeAlias = None | Tuple[str, Type[Exception]]

_base_message: str = 'verification password string'


def check_password_string(value: Any,
                          min_password: int, max_password: int,
                          message_value: str, message_type: str) -> T:

    if isinstance(value, str):
        value = value.strip()
        if len(value) == 0:
            _message: str = message_value.format(_base_message, 'cannot be whitespace or empty')

        if len(value) < min_password:
            _message: str = message_value.format(_base_message, f'cannot be less then "{min_password}"')
            return _message, ValueError

        elif len(value) > max_password:
            _message: str = message_value.format(_base_message, f'cannot be greater then "{max_password}"')
            return _message, ValueError

        return None

    _message: str = message_type.format(_base_message, 'str', TypeError.__name__)
    return _message, TypeError
