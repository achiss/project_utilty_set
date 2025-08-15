from typing import TypeAlias, Type, Tuple, Callable
from uuid import UUID


S: TypeAlias = str | UUID
T: TypeAlias = S | Tuple[str, Type[Exception]]


def convert_uuid(value: S,
                 reference_type: type | None,
                 const_chars_number_uuid: int,
                 template_regex_uuid,
                 message_type: str,
                 message_value: str,
                 message_unexpected: str,
                 func_processing_value_type: Callable,
                 func_check_reference_type: Callable,
                 func_force_converting: Callable,
                 func_soft_converting: Callable) -> T:

    _message_base_method: str = 'Convert UUID failed'

    _value_type: bool | Tuple[str, Type[Exception]] = func_processing_value_type(
        value, const_chars_number_uuid, template_regex_uuid, _message_base_method, message_type, message_value)
    if tuple == _value_type:
        return _value_type

    if _checked_result := func_check_reference_type(value, _message_base_method, message_type) is not None:
        return _checked_result

    if not reference_type:
        return func_force_converting(value, _value_type, _message_base_method, message_unexpected)

    return func_soft_converting(value, _value_type, reference_type, _message_base_method, message_unexpected)
