"""
Processing uuid: core model - generate uuid (folder)
Method: generate_uuid5
"""

from uuid import UUID
from uuid import uuid5
from typing import Tuple


def generate_uuid5(domain: UUID,
                   object_string: str,
                   msg_unexpected_error: str) -> Tuple[bool, UUID | str, None | str]:
    """
    Method: generating uuid number (uuid5)

    Args:
        domain (UUID): base uuid (used in uuid generation)
        object_string (str): object data (used in uuid generation)
        msg_unexpected_error (str): exception message

    Returns:
        Tuple[bool, UUID | str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid value if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    try:
        _result: UUID = uuid5(namespace=domain, name=object_string)
        return True, _result, None

    except Exception as e:
        _message: str = msg_unexpected_error.format(':', e)
        return False, _message, type(e).__name__
