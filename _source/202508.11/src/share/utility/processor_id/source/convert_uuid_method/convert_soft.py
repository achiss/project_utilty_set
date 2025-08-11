from typing import TypeAlias, Tuple, Type
from uuid import UUID


T: TypeAlias = Tuple[bool, UUID | str, Type[Exception] | None]


def convert_soft(value: UUID | str, value_type: bool, reference_type: bool) -> T:

    from data.message import MESSAGE_UNEXPECTED_ERROR

    _func_message: str = 'uuid value converting'

    try:
        if value_type == reference_type:
            return True, value, None

        if value_type:
            _result: str = str(value)
            return True, _result, None

        _result: UUID = UUID(value)
        return True, _result, None

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, e)
        return False, _message, type(e)
