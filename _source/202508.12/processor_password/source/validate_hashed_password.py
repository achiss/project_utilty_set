from typing import TypeAlias, Tuple, Type, Any

from data.settings import PASS_HASH_SIZE, PASS_PREFIX_STRING


T: TypeAlias = None | Tuple[str, Type[Exception]]

BASE_MESSAGE: str = 'validate hashed password'


def validate_hashed_password(value: Any,
                             message_type: str, message_value: str, message_unexpected: str) -> T:

    try:
        if isinstance(value, bytes):
            if len(value) == PASS_HASH_SIZE and value.startswith(PASS_PREFIX_STRING):
                return None

            _message: str = message_value.format(BASE_MESSAGE, f'should be equal "{PASS_HASH_SIZE}"')
            return _message, ValueError

        else:
            _message: str = message_type.format(BASE_MESSAGE, 'str', type(value).__name__)
            return _message, TypeError

    except Exception as e:
        _message: str = message_unexpected.format(BASE_MESSAGE, e)
        return _message, type(e)
