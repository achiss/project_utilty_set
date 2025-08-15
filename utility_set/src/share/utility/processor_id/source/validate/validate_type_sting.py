from typing import TypeAlias, Type, Tuple
from re import Pattern


T: TypeAlias = bool | Tuple[str, Type[Exception]]


def validate_type_string(value: str,
                         is_common_check: bool,
                         template_uuid: Pattern,
                         template_uuid4: Pattern,
                         template_uuid5: Pattern,
                         base_message: str,
                         message_unexpected: str) -> T:

    try:
        if is_common_check:
            _result: bool = bool(template_uuid.match(value))
            return _result

        _result: bool = bool(template_uuid4.fullmatch(value)) or bool (template_uuid5.fullmatch(value))
        return _result

    except Exception as e:
        _message: str = message_unexpected.format(base_message, e)
        return _message, type(e)
