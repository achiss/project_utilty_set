from typing import overload
from typing import Any, Tuple, Type
from uuid import UUID

from src.share.utility.processor_id.source import (
    generate_uuid, processing_object_data, generate_uuid4, generate_uuid5, validate_uuid, validate_type_string,
    convert_uuid, soft_converting, force_converting, processing_value_type, check_reference_type)
from data.settings import REGEX_UUID, REGEX_UUID4, REGEX_UUID5, CHARS_NUMBER_UUID
from data.message import MSG_TYPE_ERROR, MSG_UNEXPECTED_ERROR, MSG_VALUE_ERROR

from src.core_model import ExceptionID

class ProcessorID:
    __slots__ = ()

    @staticmethod
    @overload
    def convert_id(uuid_value: str | UUID) -> str | UUID: ...

    @staticmethod
    @overload
    def convert_id(uuid_value: str | UUID, reference_type: type) -> str | UUID: ...

    @staticmethod
    def convert_id(uuid_value: str | UUID = None, reference_type: type = None) -> str | UUID:

        _result: str | UUID | Tuple[str, Type[Exception]] = convert_uuid(
            uuid_value,
            reference_type=reference_type,
            const_chars_number_uuid=CHARS_NUMBER_UUID,
            template_regex_uuid=REGEX_UUID,
            message_type=MSG_TYPE_ERROR,
            message_value=MSG_VALUE_ERROR,
            message_unexpected=MSG_UNEXPECTED_ERROR,
            func_processing_value_type=processing_value_type,
            func_check_reference_type=check_reference_type,
            func_force_converting=force_converting,
            func_soft_converting=soft_converting,
        )

        print(_result)
        print(type(_result))

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

    @staticmethod
    @overload
    def validate_id(uuid_value: UUID) -> bool: ...

    @staticmethod
    @overload
    def validate_id(uuid_value: str, is_common_check: bool) -> bool: ...

    @staticmethod
    def validate_id(uuid_value: str | UUID = None, is_common_check: bool = None):

        _result: bool | Tuple[str, Type[Exception]] = validate_uuid(
            uuid_value,
            is_common_check,
            uuid_characters_number=CHARS_NUMBER_UUID,
            template_uuid=REGEX_UUID,
            template_uuid4=REGEX_UUID4,
            template_uuid5=REGEX_UUID5,
            message_type=MSG_TYPE_ERROR,
            message_value=MSG_VALUE_ERROR,
            message_unexpected=MSG_UNEXPECTED_ERROR,
            func_validate_type_string=validate_type_string,
        )

        if not bool == type(_result):
            raise ExceptionID(_result[1], _result[0])

        return _result


if __name__ == "__main__":
    _id_1 = ProcessorID.generate_id()
    _id_2 = ProcessorID.generate_id('test data', 123, object_domain=_id_1)

    _convert_1 = ProcessorID.convert_id()
