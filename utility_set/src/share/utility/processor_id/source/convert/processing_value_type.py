from typing import TypeAlias, Type, Tuple, Any
from uuid import UUID
from re import Pattern


T: TypeAlias = bool | Tuple[str, Type[Exception]]


def processing_value_type(value: Any,
                          chars_number_uuid: int,
                          template_uuid: Pattern,
                          base_message: str,
                          message_type: str,
                          message_value: str) -> T:

    """
    Note:
        False - string data type;
        True - UUID data type.
    """

    _method_name: str = '(method: processing value type)'

    if str == type(value):
        if len(value) != chars_number_uuid:
            _message: str = message_value.format(
                f'{base_message} {_method_name}',
                f'incorrect uuid string length, expected {chars_number_uuid}, got {len(value)}')
            return _message, ValueError

        if not bool(template_uuid.match(value)):
            _message: str = message_value.format(
                f'{base_message} {_method_name}',
                'incorrect uuid string format')

        return False

    elif UUID == type(value):
        return True

    else:
        _message: str = message_type.format(
            f'{base_message} {_method_name}', 'str or UUID', 'TypeError')
        return _message, TypeError
