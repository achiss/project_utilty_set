from typing import TypeAlias, Type, Tuple, Any
from uuid import UUID


T: TypeAlias = None | Tuple[str, Type[Exception]]


def check_reference_type(value: Any,
                         message_base_method: str,
                         message_type: str) -> T:

    """
    Note:
        None if succeeded
    """

    _method_name: str = '(method: check reference type)'

    if str == value or UUID == value:
        return None

    else:
        _message: str = message_type.format(
            f'{message_base_method} {_method_name}', 'str or UUID', 'TypeError')
        return _message, TypeError
