from uuid import UUID
from typing import overload
from typing import Tuple, Type


def uuid_to_string(value: UUID, to_string: bool, message: str) -> Tuple[bool, UUID | str, Type[Exception] | None]:

    if to_string:
        try:
            return True, str(value), None

        except Exception as e:
            _msg: str = message.format(':', e)
            return False, _msg, type(e)

    return True, value, None


def string_to_uuid(value: str, to_uuid: bool, message: str) -> Tuple[bool, UUID | str, Type[Exception] | None]:

    if to_uuid:
        try:
            return True, UUID(value), None

        except Exception as e:
            _msg: str = message.format(':', e)
            return False, _msg, type(e)

    return True, value, None


@overload
def convert(value: UUID, to_string: bool) -> Tuple[bool, UUID | str, Type[Exception] | None]: ...


@overload
def convert(value: str, to_uuid: bool) -> Tuple[bool, UUID | str, Type[Exception] | None]: ...


def convert(value: UUID | str = None,
            to_uuid: bool = False, to_string: bool = False) -> Tuple[bool, UUID | str, Type[Exception] | None]:

    from data import MSG_UNEXPECTED_ERROR

    if isinstance(value, UUID):
        return uuid_to_string(value, to_string, MSG_UNEXPECTED_ERROR)

    if isinstance(value, str):
        return string_to_uuid(value, to_uuid, MSG_UNEXPECTED_ERROR)

    else:
        _msg: str = MSG_UNEXPECTED_ERROR.format('', '').strip()
        return False, MSG_UNEXPECTED_ERROR, Exception
