from typing import TypeAlias, Type, Tuple, Any


T: TypeAlias = None | Tuple[str, Type[Exception]]

_base_message: str = 'verification hashed password'


def check_hashed_password(value: Any,
                          hash_size: int,
                          message_value: str,
                          message_type: str) -> T:

    if bytes == type(value):
        if len(value) != hash_size:
            _message: str = message_value.format(_base_message, f'should be equal to "{hash_size}" characters')
            return _message, ValueError

        return None

    _message: str = message_type.format(_base_message, 'bytes', TypeError.__name__)
    return _message, TypeError
