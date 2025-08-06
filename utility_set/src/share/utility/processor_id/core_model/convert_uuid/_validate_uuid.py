"""
Utility method: verification converting method
"""

from uuid import UUID
from typing import Tuple
from re import Pattern


def validate_uuid(value: UUID | str,
                  is_common_verification: bool,
                  regex_common: Pattern,
                  regex_uuid4: Pattern,
                  regex_uuid5: Pattern,
                  message_type: str,
                  message_value: str,) -> Tuple[bool, bool | str, None | str]:

    if isinstance(value, UUID):
        return True, True, None

    elif isinstance(value, str):
        if len(value) != 32 or len(value) != 36:
            _message: str = message_value.format('length should be 32 or 36 characters long')
            return False, _message, ValueError.__name__

        if is_common_verification and not regex_common.match(value):
            _message: str = message_value.format('value should be match regex common uuid pattern')
            return False, _message, ValueError.__name__

        if not (is_common_verification and (regex_uuid4.match(value) or regex_uuid5.match(value))):
            _message: str = message_value.format('value should be match regex uuid4 or uuid5 patterns')
            return False, _message, ValueError.__name__

        return True, False, None

    _message: str = message_type.format('UUID or str', type(value).__name__)
    return False, _message, TypeError.__name__
