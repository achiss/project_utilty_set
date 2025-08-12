from typing import TypeAlias, Type, Tuple, Callable

from bcrypt import gensalt, hashpw


T: TypeAlias = bytes | Tuple[str, Type[Exception]]
Y: TypeAlias = None | Tuple[str, Type[Exception]]

_base_message: str = 'generating hash password'


def generate_password_hash(value: str,
                           min_password: int,
                           max_password: int,
                           iteration_number: int,
                           prefix_string: bytes,
                           message_value: str,
                           message_type: str,
                           message_unexpected: str,
                           check_password: Callable) -> T:

    _checked_att: Y = check_password(value, min_password, max_password, message_value, message_type)
    if None != _checked_att:
        return _checked_att

    try:
        _salt: bytes = gensalt(rounds=iteration_number, prefix=prefix_string)
        _password: bytes = value.encode(encoding='utf-8')
        return hashpw(password=_password, salt=_salt)

    except Exception as e:
        _message: str = message_unexpected.format(_base_message, e)
        return _message, type(e)
