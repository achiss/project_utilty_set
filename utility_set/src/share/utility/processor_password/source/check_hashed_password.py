from typing import TypeAlias, Type, Tuple, Any


T: TypeAlias = None | Tuple[str, Type[Exception]]

_base_message: str = 'verification hashed password'


def check_hashed_password(value: Any,
                          prefix_string: bytes,
                          message_value: str,
                          message_type: str) -> T:

    if bytes == type(value):
        if len(value) != 60:
            _message: str = message_value.format(_base_message, 'should be equal to 60 characters')
            return _message, ValueError

        if not value.startswith(prefix=prefix_string):
            _message: str = message_value.format(_base_message, f'should be start with "{prefix_string}"')
            return _message, ValueError

        return None

    _message: str = message_type.format(_base_message, 'bytes', TypeError.__name__)
    return _message, TypeError
