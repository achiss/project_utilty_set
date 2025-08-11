"""
Processing ID (core): validate uuid
Methods:
    validate_id
"""

from uuid import UUID
from typing import Tuple
from typing import overload


@overload
def validate_id(value: UUID) -> Tuple[bool, bool | str, None | str]: ...


@overload
def validate_id(value: str,
                is_common_check: bool) -> Tuple[bool, bool | str, None | str]: ...


def validate_id(value: UUID | str = None,
                is_common_check: bool = None) -> Tuple[bool, bool | str, None | str]:
    """
    Method: checking the string for the fact that it is a UUID

    Args:
        value (UUID): data type value
        is_common_check (bool): used for the str data type
            (if True, it is checked for compliance with any uuid, otherwise uuid4 and uuid5 are checked)

    Returns:
        Tuple[bool, bool | str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: True if it matches the pattern (or the UUID data type) if it succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    from data import MESSAGE_UNEXPECTED_ERROR_ID, REGEX_UUID, REGEX_UUID4, REGEX_UUID5
    from src.share.utility.processing_uuid.core_model.check_data_type import check_data_type
    from src.share.utility.processing_uuid.core_model.validate_uuid_method import (check_string_uuid_common,
                                                                                   check_string_uuid)

    _base_message: str = 'Failed ID conversion'
    _message: str = f'{_base_message}: {MESSAGE_UNEXPECTED_ERROR_ID}'

    if not (_result := check_data_type(value))[0]:
        return _result

    if isinstance(value, UUID):
        return True, True, None

    if is_common_check:
        return check_string_uuid_common(value, regex=REGEX_UUID, message=_message)

    else:
        return check_string_uuid(value, regex_uuid4=REGEX_UUID4, regex_uuid5=REGEX_UUID5, message=_message)
