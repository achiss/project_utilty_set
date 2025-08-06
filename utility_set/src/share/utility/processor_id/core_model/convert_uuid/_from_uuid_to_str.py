"""
Utility method: converting str data type to UUID
"""

from typing import Tuple
from uuid import UUID


def from_uuid_to_str(value: UUID,
                     message_unexpected: str) -> Tuple[bool, str, None | str]:

    try:
        _result: str = value.__str__()
        return True, _result, None

    except Exception as e:
        _message: str = message_unexpected.format('-', e)
        return  False, _message, type(e).__name__
