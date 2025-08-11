from typing import TypeAlias, Tuple, Type, Any
from uuid import UUID

T: TypeAlias = Tuple[bool, str | bool, Type[Exception] | None]


def support_check_argument(value: Any, as_uuid: bool, as_str: bool) -> bool:

    from data.conf import REGEX_UUID

    if not (as_uuid and as_str):
        raise AttributeError

    if isinstance(value, UUID) and as_uuid:
        return True

    elif isinstance(value, str) and as_str:
        if len(value) not in (32, 36):
            raise ValueError('does not match the specified number of characters')

        if not REGEX_UUID.fullmatch(value):
            raise ValueError('does not match the specified format')

        return False

    raise TypeError


def verify_uuid_value(value: Any, as_uuid: bool = True, as_str: bool = True) -> 'T':
    """
    Args:
        value (Any): check value.
        as_uuid (bool): True, check UUID, False, no action. (default: True)
        as_str (bool): True, check string. False, no action. (default: True)

    Returns:
        -   If operation succeeded - True, False otherwise.
        -   If operation succeeded and received data type UUID - True, False - str. If operation failed return error message.
        -   IF operation succeeded - None. If operation failed return exception type.
    """

    from data.message import MESSAGE_ATTRIBUTE_ERROR, MESSAGE_TYPE_ERROR, MESSAGE_VALUE_ERROR, MESSAGE_UNEXPECTED_ERROR

    _func_message: str = 'verify uuid value method'

    try:
        _result = support_check_argument(value, as_uuid, as_str)
        if not _result:
            return True, False, None

        return True, True, None

    except AttributeError:
        _message: str = MESSAGE_ATTRIBUTE_ERROR.format(
            _func_message, '(as_uuid and as_str)', 'cannot be False at the same time')
        return False, _message, AttributeError

    except TypeError:
        _message: str = MESSAGE_TYPE_ERROR.format(_func_message, 'UUID or str', type(value).__name__)
        return False, _message, TypeError

    except ValueError as e:
        _message: str = MESSAGE_VALUE_ERROR.format(_func_message, str(e)).strip()
        return False, _message, ValueError

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, str(e)).strip()
        return False, _message, type(e)
