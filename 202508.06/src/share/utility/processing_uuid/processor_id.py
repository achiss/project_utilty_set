from typing import Tuple, Type, Any, List
from uuid import UUID

from src.share.utility.processing_uuid.script.convert import convert
from src.share.utility.processing_uuid.script.generate import generate
from src.share.utility.processing_uuid.script.validate import validate


class ProcessorID:
    __slots__ = ()

    # Section: convert uuid
    @staticmethod
    def __convert_verification(uuid_value: UUID | str,
                               to_uuid: bool | None,
                               to_string: bool | None,
                               base_message: str) -> Tuple[bool, UUID | str | None, Type[Exception] | None]:

        if not isinstance(uuid_value, (UUID, str)):
            _msg: str = f'{base_message}: invalid data type - expected "UUID, str", got "{type(uuid_value)}"'
            return False, _msg, TypeError

        if not (isinstance(to_uuid, (bool, type(None))) or isinstance(to_string, (bool, type(None)))):
            _msg: str = f'{base_message}: invalid data type - expected "bool, None", got "{type(uuid_value)}"'
            return False, _msg, TypeError

        if (to_uuid and to_string) or (to_uuid and to_string) is None:
            _msg: str = f'{base_message}: invalid attributes - "to_uuid, to_string" cannot be defined at the same time'
            return False, _msg, AttributeError

        if isinstance(uuid_value, UUID) and not to_string:
            _msg: str = f'{base_message}: invalid attributes - if the data type is "UUID", the attribute "to_string" should be defined'
            return False, _msg, AttributeError

        if isinstance(uuid_value, str) and not to_uuid:
            _msg: str = f'{base_message}: invalid attributes - if the data type is "str", the attribute "to_uuid" should be defined'
            return False, _msg, AttributeError

        return True, None, None

    @staticmethod
    def convert(uuid_value: UUID | str,
                to_uuid: bool | None,
                to_string: bool | None) -> Tuple[bool, UUID | str, Type[Exception] | None]:

        base_message: str = 'Processing ID (operation: convert) failed'

        if not (result := ProcessorID.__convert_verification(uuid_value, to_uuid, to_string, base_message))[0]:
            return result

        try:
            if to_uuid is None:
                return convert(value=uuid_value, to_string=to_string)

            return convert(value=uuid_value, to_uuid=to_uuid)

        except Exception as e:
            _msg: str = f'{base_message}: unexpected error - {e}'
            return False, _msg, type(e)

    # Section: generate uuid
    @staticmethod
    def __generate_verification(*name_value: Any,
                                domain_value: UUID | None,
                                base_message: str) -> Tuple[bool, UUID | str | None, Type[Exception] | None]:

        if not isinstance(domain_value, (UUID, type(None))):
            _msg: str = f'{base_message}: invalid data type - expected "UUID, None", got "{type(domain_value)}'
            return False, _msg, TypeError

        if isinstance(domain_value, UUID) and len(name_value) == 0:
            _msg: str = f'{base_message}: invalid attributes - "domain_value" requires non-empty "name_value"'
            return False, _msg, AttributeError

        elif domain_value is None and len(name_value) != 0:
            _msg: str = f'{base_message}: invalid attributes - "name_value" requires "domain_value"'
            return False, _msg, AttributeError

        return True, None, None

    @staticmethod
    def __generate_processing_name(*name_value: Any,
                                   base_message: str) -> Tuple[bool, str, Type[Exception] | None]:

        if len(name_value) == 1:
            return True, str(name_value[0]), None

        try:
            name_list: List[str] = []
            for _arg in name_value:
                name_list.append(str(_arg))

            return True, ', '.join(name_list), None

        except Exception as e:
            _msg: str = f'{base_message}: unexpected error during args processing - {e}'
            return False, _msg, type(e)

    @staticmethod
    def generate(*name_value: Any,
                 domain_value: UUID | None) -> Tuple[bool, UUID | str, Type[Exception] | None]:

        base_message: str = 'Processing ID (operation: generate) failed'

        if not (result := ProcessorID.__generate_verification(
                name_value, domain_value=domain_value, base_message=base_message))[0]:
            return result

        if len(name_value) > 0:
            if not (result := ProcessorID.__generate_processing_name(
                    name_value, base_message=base_message))[0]:
                return result

            name_value: str = result[1].strip()
        try:
            if len(name_value) == 0:
                return generate()

            return generate(object_value=name_value, domain=domain_value)

        except Exception as e:
            _msg: str = f'{base_message}: unexpected error - {e}'
            return False, _msg, type(e)

    # Section: validate uuid
    @staticmethod
    def __validate_verification(uuid_value: UUID | str,
                                is_general_verification: bool | None,
                                base_message: str) -> Tuple[bool, str | None, Type[Exception] | None]:

        if not isinstance(uuid_value, (UUID, str)):
            _msg: str = f'{base_message}: invalid data type - expected "UUID, str", got "{type(uuid_value)}"'
            return False, _msg, TypeError

        if not isinstance(is_general_verification, (bool, type(None))):
            _msg: str = f'{base_message}: invalid data type - expected "bool, None", got "{type(is_general_verification)}"'
            return False, _msg, TypeError

        if isinstance(uuid_value, UUID) and is_general_verification is not None:
            _msg: str = f'{base_message}: invalid attribute - if data type is "UUID" attribute should not be defined'
            return False, _msg, AttributeError

        if isinstance(uuid_value, str) and is_general_verification is None:
            _msg: str = f'{base_message}: invalid attribute - if data type is "str" attribute should be defined'
            return False, _msg, AttributeError

        return True, None, None

    @staticmethod
    def validate(uuid_value: UUID | str,
                 is_general_verification: bool | None) -> Tuple[bool, bool | str, Type[Exception] | None]:

        base_message: str = 'Processing ID (operation: validate) failed'

        if not (result := ProcessorID.__validate_verification(uuid_value, is_general_verification, base_message))[0]:
            return result

        try:
            return validate(value=uuid_value, is_common=is_general_verification)

        except Exception as e:
            _msg: str = f'{base_message}: unexpected error - {e}'
            return False, _msg, type(e)


if __name__ == '__main__':
    _id = ProcessorID.generate()
    print(_id)
