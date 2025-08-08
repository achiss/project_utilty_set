"""
Script (processing id - generate uuid): generate uuid.
"""

from typing import Tuple, Any
from uuid import UUID

from src.share.utility.processor_id.utility_model.generate_uuid._base_generating import generate_uuid4, generate_uuid5
from src.share.utility.processor_id.utility_model.generate_uuid._verification_argument import \
    verification_argument_object_data, verification_argument_object_domain
from src.share.utility.processor_id.utility_model.generate_uuid._processing_argument import \
    processing_argument_object_data


T: type[tuple] = Tuple[bool, UUID | str, None | str]


def generate_uuid(*object_data: Any,
                  object_domain: Any) -> T:
    """
    ID generation method (used: uuid4 | uuid5)

    Args:
        *object_data (Any): data object arguments value(s) (used for uuid5)
        object_domain (UUID): domain object value (used for uuid5)

    Returns:
        Tuple[bool, UUID | str, None | str]
            -   if operation succeed - True, otherwise False;
            -   if generating succeed - uuid number, otherwise exception message;
            -   if generating succeed - None, otherwise name string of exception type.
    """

    if object_domain is None:
        _flag, _data, _e = generate_uuid4()
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

        return generate_uuid5(object_data=_data, object_domain=object_domain)


if __name__ == '__main__':
    print(generate_uuid(object_domain=None))
