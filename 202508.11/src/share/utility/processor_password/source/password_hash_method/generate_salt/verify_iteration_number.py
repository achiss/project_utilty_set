from typing import TypeAlias, Tuple, Type, Any

T: TypeAlias = Tuple[bool, bool | str, Type[Exception] | None]


def verify_iteration_number(value: Any) -> 'T':

    from data.message import MESSAGE_TYPE_ERROR, MESSAGE_UNEXPECTED_ERROR

    _func_message: str = ''

    try:
        if isinstance(value, int):
            if value < 1:
                pass

            elif value > 31:
                pass

            else:
                _message: str = ''
                return False, _message, ValueError

        else:
            _message: str = ''
            return False, _message, None

        return True, True, None

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, e)
        return False, _message, type(e)
