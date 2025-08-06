"""
Processing uuid: core model - checking methods (folder)
Method: check data type
"""

from uuid import UUID

def check_data_type(value: UUID | str,
                    as_string: bool = True,
                    as_uuid: bool = True) -> bool | None:
    """
    Method: checks the UUID or str data type

    Args:
        value (UUID): checked value
        as_string (bool): verify data type as str (default: True)
        as_uuid (bool): verify data type as UUID (default: True)

    Returns:
        bool: True if succeeded, False otherwise (None if incorrect conditions)
    """

    if not (as_string and as_uuid):
        return None

    if as_string and not as_uuid:
        return isinstance(value, str)

    elif not as_string and as_uuid:
        return isinstance(value, UUID)

    return isinstance(value, (UUID, str))
