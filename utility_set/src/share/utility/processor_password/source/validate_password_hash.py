from typing import TypeAlias, Type, Tuple, Callable

from bcrypt import checkpw


T: TypeAlias = bool | Tuple[str, Type[Exception]]
Y: TypeAlias = None | Tuple[str, Type[Exception]]

_base_message = 'validating hashed password'


def validate_password_hash(value: str,
                           hashed_value: bytes,
                           prefix_string: bytes,
                           min_password: int,
                           max_password: int,
                           message_value: str,
                           message_type: str,
                           message_unexpected: str,
                           check_password: Callable,
                           check_hashed_password: Callable) -> T:

    _checked_password_string: Y = check_password(
        value, min_password, max_password, message_value, message_type)
    if None != _checked_password_string:
        return _checked_password_string

    _checked_hashed_password: Y = check_hashed_password(
        hashed_value, prefix_string, message_value, message_type)
    if None != _checked_hashed_password:
        return _checked_hashed_password

    try:
        _password: bytes = value.encode(encoding='utf-8')
        return checkpw(password=_password, hashed_password=hashed_value)

    except Exception as e:
        _message: str = message_unexpected.format(_base_message, e)
        return _message, type(e)
