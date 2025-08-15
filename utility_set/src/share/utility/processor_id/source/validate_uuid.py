from typing import TypeAlias, Type, Tuple, Callable
from uuid import UUID
from re import Pattern


T: TypeAlias = bool | Tuple[str, Type[Exception]]


def validate_uuid(uuid_value: str | UUID,
                  is_common_check: bool,
                  uuid_characters_number: int,
                  template_uuid: Pattern,
                  template_uuid4: Pattern,
                  template_uuid5: Pattern,
                  message_type: str,
                  message_value: str,
                  message_unexpected: str,
                  func_validate_type_string: Callable) -> T:

    _base_message: str = 'Validate UUID failed'

    if str == type(uuid_value):
        _result: T = func_validate_type_string(
            uuid_value, is_common_check , uuid_characters_number, template_uuid, template_uuid4, template_uuid5,
            _base_message, message_value, message_unexpected)
        return _result

    elif UUID == type(uuid_value):
        return True

    else:
        _message: str = message_type.format(_base_message, 'str or UUID', type(uuid_value).__name__)
        return _message, TypeError
