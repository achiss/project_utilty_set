"""
Processor ID model
Included methods:
    -   convert
    -   generate
"""

from typing import Type, Any
from typing import overload
from uuid import UUID

from src.share.utility.processor_id.utility_model.convert_uuid import convert_uuid
from src.share.utility.processor_id.utility_model.generate_uuid import generate_uuid

from data.message import BASE_MSG_CONVERT, BASE_MSG_GENERATE
from src.core_model.exception_model import ExceptionID


class ProcessorID:
    """
    Utility: processing ID.

    Included methods:
        - convert
        - generate
    """

    __slots__ = ()

    @staticmethod
    @overload
    def convert(uuid_value: UUID | str) -> bool: ...

    @staticmethod
    @overload
    def convert(uuid_value: UUID | str,
                reference_type: Type[Any] = None) -> bool: ...

    @staticmethod
    def convert(uuid_value: UUID | str,
                reference_type: Type[Any] = None) -> bool:
        """
        Convert ID.

        Notes: if parameter (reference type) is defined, the method converts the data type otherwise method checks
        and converts the data type if it does not match the reference value.

        Args:
            uuid_value (UUID | str):
            reference_type (type):

        Returns: changed data type or same data type

        Raises: ExceptionID (custom exception class).
        """

        _flag, _data, _e = convert_uuid(uuid_value, reference_type)
        if not _flag:
            _message: str = f'{BASE_MSG_CONVERT}: {_data}.'
            raise ExceptionID(ProcessorID, _e, _message)

        return _data

    @staticmethod
    @overload
    def generate() -> UUID: ...

    @staticmethod
    @overload
    def generate(*object_data: Any,
                  object_domain: UUID = None) -> UUID: ...

    @staticmethod
    def generate(*object_data: Any,
                  object_domain: UUID = None) -> UUID:
        """
        Generate ID.

        Notes: if no parameters using uuid4 method, else using uuid5 method.

        Args:
            object_data (Any): arguments value for generate uuid5.
            object_domain (UUID): domain value for generate uuid5.

        Returns: ID value (UUID).

        Raises: ExceptionID (custom exception class).
        """

        _flag, _data, _e = generate_uuid(object_data, object_domain=object_domain)
        if not _flag:
            _message: str = f'{BASE_MSG_GENERATE}: {_data}.'
            raise ExceptionID(ProcessorID, _e, _message)

        return _data


if __name__ == '__main__':
    _id = ProcessorID.generate()
    print(_id)
