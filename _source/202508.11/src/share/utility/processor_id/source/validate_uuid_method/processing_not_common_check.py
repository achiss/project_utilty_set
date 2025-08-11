from typing import TypeAlias, Tuple, Type

T: TypeAlias = Tuple[bool, bool | str, Type[Exception] | None]


def processing_not_common_check(value: str) -> 'T':

    from data.message import MESSAGE_UNEXPECTED_ERROR, MESSAGE_VALUE_ERROR
    from data.conf import REGEX_UUID4, REGEX_UUID5

    _func_message: str = 'processing parameter "is_common" for uuid string verification'

    try:
        if not (REGEX_UUID4.fullmatch(string=value) or REGEX_UUID5.fullmatch(string=value)):
            raise ValueError('does not match the uui4 or uuid5 formats')

        return True, True, None

    except ValueError as e:
        _message: str = MESSAGE_VALUE_ERROR.format(_func_message, str(e)).strip()
        return False, _message, ValueError

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, e)
        return False, _message, type(e)
