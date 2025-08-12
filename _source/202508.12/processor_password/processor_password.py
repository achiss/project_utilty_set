from typing import TypeAlias, Tuple, Type

from src.share.utility.processor_password.source import (
    generate_hash, validate_hash, validate_password_string, validate_hashed_password)

from data.settings import PASS_MIN_LENGTH, PASS_MAX_LENGTH, PASS_HASH_SIZE, PASS_ITERATION_NUMBER, PASS_PREFIX_STRING
from data.message import MSG_TYPE_ERROR, MSG_VALUE_ERROR, MSG_UNEXPECTED_ERROR


T: TypeAlias = bytes | Tuple[str, Type[Exception]]


class ProcessorPassword:
    __slots__ = ()

    @staticmethod
    def generate_hash(password_string: str) -> bytes:

        _result_operation: T = generate_hash(
            password_string,
            message_type=MSG_TYPE_ERROR,
            message_value=MSG_VALUE_ERROR,
            message_unexpected=MSG_UNEXPECTED_ERROR,
            check_password_string=validate_password_string,
            iteration_number=PASS_ITERATION_NUMBER,
            prefix_string=PASS_PREFIX_STRING,
        )
        return _result_operation

    @staticmethod
    def validate_hash(password_string: str, hashed_password: bytes) -> bool: pass


if __name__ == '__main__':
    _hash = ProcessorPassword.generate_hash(password_string='1')
    print(_hash)
