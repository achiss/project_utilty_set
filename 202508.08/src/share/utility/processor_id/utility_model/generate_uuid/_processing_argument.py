"""
Script (processing id - generate uuid): processing argument data.
"""

from typing import Tuple, Any, List

T: type[tuple] = Tuple[bool, str, None | str]


def processing_argument_object_data(*args: Any) -> T:
    """
    Processing args (object_data) method.

    Args:
        args (Any): processing arguments

    Returns:
        Tuple[bool, str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if processing succeed - arguments string, otherwise exception message;
            -   if processing succeed - None, otherwise name string of exception type.
    """

    from data.message import MSG_DATA_TYPE_ERROR, MSG_VALUE_ERROR, MSG_UNEXPECTED_ERROR

    _converted_list: List[str] = []
    try:
        for _arg in args:
            try:
                _converted_list.append(str(_arg))

            except TypeError:
                _message = MSG_DATA_TYPE_ERROR.format('convertable to str type', type(_arg).__name__)
                return False, _message, TypeError.__name__

            except ValueError as e:
                _message = MSG_VALUE_ERROR.format(f'during converting argument to str - {e}')
                return False, _message, ValueError.__name__

        _converted_list: str = ' '.join(_converted_list).strip()
        if len(_converted_list) == 0:
            _message: str = MSG_VALUE_ERROR.format('data for parameter "object data" should be defined')
            return False, _message, ValueError.__name__

        return True, _converted_list, None

    except Exception as e:
        _message: str = MSG_UNEXPECTED_ERROR.format('-', e)
        return False, _message, type(e).__name__
