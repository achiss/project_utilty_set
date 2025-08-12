from typing import TypeAlias, Type, Tuple

from src.share.utility.processor_password.source import (
    generate_password_hash, validate_password_hash, check_password_string, check_hashed_password)

from data.settings import PASS_MIN_LENGTH, PASS_MAX_LENGTH, PASS_ITERATION_NUMBER, PASS_PREFIX_STRING
from data.message import MSG_TYPE_ERROR, MSG_VALUE_ERROR, MSG_UNEXPECTED_ERROR


T: TypeAlias = bytes | Tuple[str, Type[Exception]]
YG: TypeAlias = bytes | Tuple[str, Type[Exception]]
YV: TypeAlias = bool | Tuple[str, Type[Exception]]


class ProcessorPassword:
    __slots__ = ()

    @staticmethod
    def generate_hash(password_string: str) -> bytes:

        _result: YG = generate_password_hash(
            password_string,
            min_password=PASS_MIN_LENGTH,
            max_password=PASS_MAX_LENGTH,
            iteration_number=PASS_ITERATION_NUMBER,
            prefix_string=PASS_PREFIX_STRING,
            message_type=MSG_TYPE_ERROR,
            message_value=MSG_VALUE_ERROR,
            message_unexpected=MSG_UNEXPECTED_ERROR,
            check_password=check_password_string)

        if bytes != type(_result):
            raise _result[1](_result[0])

        return _result

    @staticmethod
    def validate_hash(password_string: str,
                      hashed_password: bytes) -> bool:

        _result: YV = validate_password_hash(
            password_string,
            hashed_password,
            prefix_string=PASS_PREFIX_STRING,
            min_password=PASS_MIN_LENGTH,
            max_password=PASS_MAX_LENGTH,
            message_value=MSG_VALUE_ERROR,
            message_type=MSG_TYPE_ERROR,
            message_unexpected=MSG_UNEXPECTED_ERROR,
            check_password=check_password_string,
            check_hashed_password=check_hashed_password,
        )

        if bool != type(_result):
            raise _result[1](_result[0])

        return _result


if __name__ == '__main__':
    _hash = ProcessorPassword.generate_hash('12345678')
    print(_hash)
