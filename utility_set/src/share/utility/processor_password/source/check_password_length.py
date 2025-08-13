from typing import TypeAlias, Type, Tuple, Any


T: TypeAlias = None | Tuple[str, Type[Exception]]

_base_message: str = 'verification password length'


def check_password_length(value: Any,
                          min_password: int,
                          max_password: int,
                          message_value: str,
                          message_type: str) -> T:

    if isinstance(value, int):
        if value == 0:
            _message: str = message_value.format(_base_message, 'password length should be defined')
            return _message, ValueError

        if value < min_password:
            _message: str = message_value.format(_base_message, f'cannot be less then "{min_password}"')
            return _message, ValueError

        elif value > max_password:
            _message: str = message_value.format(_base_message, f'cannot be greater then "{max_password}"')
            return _message, ValueError

        return None

    _message: str = message_type.format(_base_message, 'int', TypeError.__name__)
    return _message, TypeError
