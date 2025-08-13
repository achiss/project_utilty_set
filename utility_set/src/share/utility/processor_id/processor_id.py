from typing import overload
from typing import Any, Tuple, Type
from uuid import UUID

from src.share.utility.processor_id.source import generate_uuid, processing_object_data, generate_uuid4, generate_uuid5
from data.message import MSG_TYPE_ERROR, MSG_UNEXPECTED_ERROR

from src.core_model import ExceptionID

class ProcessorID:
    __slots__ = ()

    @staticmethod
    @overload
    def generate_id() -> UUID: ...

    @staticmethod
    @overload
    def generate_id(*object_data: Any, object_domain: UUID) -> UUID: ...

    @staticmethod
    def generate_id(*object_data: Any, object_domain: UUID = None) -> UUID:

        _result: UUID| Tuple[str | Type[Exception]] = generate_uuid(
            object_data,
            object_domain=object_domain,
            message_type=MSG_TYPE_ERROR,
            message_unexpected=MSG_UNEXPECTED_ERROR,
            generate_uuid4=generate_uuid4,
            generate_uuid5=generate_uuid5,
            processing_object_data=processing_object_data,
        )

        if UUID != type(_result):
            raise ExceptionID(_result[1], _result[0])

        return _result


if __name__ == "__main__":
    _id = ProcessorID.generate_id()
    print(_id)