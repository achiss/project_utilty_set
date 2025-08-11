from typing import TypeAlias, Tuple, Type, Any

from data.conf import PREFIX_SALT

T: TypeAlias = Tuple[bool, bool | str, Type[Exception] | None]


def verify_prefix(value: Any) -> 'T':

    from data.message import MESSAGE_TYPE_ERROR, MESSAGE_UNEXPECTED_ERROR

    _func_message: str = ''

    try:
        if not (isinstance(value, bytes) and value in PREFIX_SALT):
                _message: str = ''
                return False, _message, ValueError

        else:
            _message: str = ''
            return False, _message, TypeError

        return True, True, None

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, e)
        return False, _message, type(e)
