"""
Processing uuid: core model - generate uuid (folder)
Method: generate_uuid4
"""

from uuid import UUID
from uuid import uuid4
from typing import Tuple


def generate_uuid4(msg_unexpected_error: str) -> Tuple[bool, UUID | str, None | str]:
    """
    Method: generating uuid number (uuid4)

    Args:
        msg_unexpected_error (str): exception message

    Returns:
        Tuple[bool, UUID | str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid value if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    try:
        _result: UUID = uuid4()
        return True, _result, None

    except Exception as e:
        _message: str = msg_unexpected_error.format(':', e)
        return False, _message, type(e).__name__
