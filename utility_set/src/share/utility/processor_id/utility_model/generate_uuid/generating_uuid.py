"""
Script (processing id - generate uuid): generate uuid.
"""

from typing import Tuple, Any
from typing import overload
from uuid import UUID

from src.share.utility.processor_id.utility_model.generate_uuid._base_generating import base_generating
from src.share.utility.processor_id.utility_model.generate_uuid._verification_argument import \
    verification_argument_object_data, verification_argument_object_domain
from src.share.utility.processor_id.utility_model.generate_uuid._processing_argument import \
    processing_argument_object_data


T: type[tuple] = Tuple[bool, UUID | str, None | str]

@overload
def generate_uuid() -> T:...


@overload
def generate_uuid(*object_data: Any,
                  object_domain: UUID) -> T:...


def generate_uuid(*object_data: Any,
                  object_domain: UUID = None) -> T:
    """
    ID generation method (used: uuid4 | uuid5)

    Args:
        *object_data (Any): data object arguments value(s) (used for uuid5)
        object_domain (UUID): domain object value (used for uuid5)
    
    Returns:
        Tuple[bool, UUID | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if verification succeed - uuid number, otherwise exception message;
            -   if verification succeed - None, otherwise name string of exception type.
    """

    if not (object_data or object_domain):
        _flag, _data, _e = base_generating(object_data=None,object_domain=None)
        if not _flag:
            return False, _data, _e

        return True, _data, None

    else:
        if not (_result := verification_argument_object_data(*object_data))[0]:
            return _result

        if not (_result := verification_argument_object_domain(object_domain))[0]:
            return _result

        _flag, _data, _e = processing_argument_object_data(object_data)
        if not _flag:
            return False, _data, _e

        return base_generating(object_data=_data, object_domain=object_domain)


if __name__ == '__main__':
    pass
