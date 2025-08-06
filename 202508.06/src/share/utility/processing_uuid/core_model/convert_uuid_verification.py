"""
Processing ID (core): convert uuid
Methods:
    check_data_type
"""

from uuid import UUID


def check_data_type(value: UUID | str,
                    as_string: bool = True,
                    as_uuid: bool = True) -> bool:
    """
    Method: verify uuid data type

    Args:
        value (UUID): data type value
        as_string (bool): verify data type as str (default: True)
        as_uuid (bool): verify data type as UUID (default: True)

    Returns:
        bool: True if succeeded, False otherwise
    """

    if as_string and as_uuid:
        return isinstance(value, (UUID, str))

    elif as_string and not as_uuid:
        return isinstance(value, str)

    elif not as_string and as_uuid:
        return isinstance(value, UUID)

    return False
