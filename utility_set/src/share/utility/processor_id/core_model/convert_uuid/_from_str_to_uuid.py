"""
Utility method: converting UUID data type to str
"""

from typing import Tuple
from uuid import UUID


def from_str_to_uuid(value: str,
                     message_unexpected: str) -> Tuple[bool, UUID | str, None | str]:

    try:
        _result: UUID = UUID(value)
        return True, _result, None

    except Exception as e:
        _message: str = message_unexpected.format('-', e)
        return  False, _message, type(e).__name__
