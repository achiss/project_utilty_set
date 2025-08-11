from uuid import UUID
from typing import overload
from typing import Tuple, Type

from data import REGEX_UUID, REGEX_UUID4, REGEX_UUID5


def check_uuid_string(value: str, is_common: bool,
                      message: str) -> Tuple[bool, bool | str, Type[Exception] | None]:

    if is_common:
        try:
            if bool(REGEX_UUID.fullmatch(string=value)):
                return True, True, None

            return True, False, None

        except Exception as e:
            _msg: str = message.format(':', e)
            return False, _msg, Exception

    try:
        if bool(REGEX_UUID4.fullmatch(string=value)) or bool(REGEX_UUID5.fullmatch(string=value)):
            return True, True, None

        return True, False, None

    except Exception as e:
        _msg: str = message.format(':', e)
        return False, _msg, Exception


@overload
def validate(value: UUID) -> Tuple[bool, bool | str, Type[Exception] | None]: ...


@overload
def validate(value: str, is_common: bool) -> Tuple[bool, bool | str, Type[Exception] | None]: ...


def validate(value: UUID | str = None, is_common: bool = None) -> Tuple[bool, bool | str, Type[Exception] | None]:

    from data import MSG_UNEXPECTED_ERROR

    if isinstance(value, UUID):
        return True, True, None

    return check_uuid_string(value, is_common, MSG_UNEXPECTED_ERROR)
