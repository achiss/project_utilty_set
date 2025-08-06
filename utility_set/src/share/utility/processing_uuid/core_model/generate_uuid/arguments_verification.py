"""
Processing uuid: core model - generate uuid (folder)
Method: arguments_processing
"""

from typing import Any, Tuple, List
from uuid import UUID


def arguments_processing_domain(domain: UUID,
                                msg_attribute_error: str,
                                msg_type_error: str,
                                msg_unexpected_error: str) -> Tuple[bool, None | str, None | str]:

    from src.share.utility.processing_uuid.core_model.checking_methods.check_data_type import check_data_type

    try:
        _result: bool | None = check_data_type(domain, as_string=False)
        if _result is None:
            _message: str = msg_attribute_error.format('check data type failed')
            return False, _message, AttributeError.__name__

        if not _result:
            _message: str = msg_type_error.format('UUID', type(domain).__name__)
            return False, _message, TypeError.__name__

        return True, None, None

    except Exception as e:
        _message: str = msg_unexpected_error.format(':', e)
        return False, _message, type(e).__name__
