"""
Processing ID (core): convert uuid
Methods:
    from_uuid_to_string
    from_string_to_uuid
"""

from uuid import UUID
from typing import Tuple


def from_uuid_to_string(value: UUID,
                        message: str) -> Tuple[bool, str, str | None]:
    """
    Method: convert UUID data type to string data type

    Args:
        value (UUID): data type value
        message (str): exception message

    Returns:
        Tuple[bool, str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid in string data type if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    try:
        _result = value.__str__()
        return True, _result, None

    except Exception as e:
        _message: str = message.format(':', e)
        return False, _message, type(e).__name__


def from_string_to_uuid(value: str,
                        message: str) -> Tuple[bool, UUID | str, str | None]:
    """
    Method: convert string data type to UUID data type

    Args:
        value (str): data type value
        message (str): exception message

    Returns:
        Tuple[bool, str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: uuid in UUID data type if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    try:
        _result = UUID(value)
        return True, _result, None

    except Exception as e:
        _message: str = message.format(':', e)
        return False, _message, type(e).__name__


if __name__ == "__main__":
    pass
