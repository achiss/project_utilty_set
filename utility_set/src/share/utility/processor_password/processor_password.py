from typing import TypeAlias, Type, Tuple

from src.share.utility.processor_password.source import (
    generate_password_hash, validate_password_hash, check_password_string, check_hashed_password,
    generate_password_string, get_char_list_digits, get_char_list_special, get_password_string, check_password_length)

from data.settings import (
    PASS_MIN_LENGTH, PASS_MAX_LENGTH, PASS_ITERATION_NUMBER, PASS_PREFIX_STRING, PASS_HASH_SIZE, SPECIAL_CHARS)
from data.message import MSG_TYPE_ERROR, MSG_VALUE_ERROR, MSG_UNEXPECTED_ERROR

from src.core_model import ExceptionPassword


T: TypeAlias = bytes | Tuple[str, Type[Exception]]
YG: TypeAlias = bytes | Tuple[str, Type[Exception]]
YV: TypeAlias = bool | Tuple[str, Type[Exception]]
GS: TypeAlias = str | Tuple[str, Type[Exception]]


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
            raise ExceptionPassword(_result[1], _result[0])

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
            raise ExceptionPassword(_result[1], _result[0])

        return _result

    @staticmethod
    def generate_password_string(password_length: int,
                                 use_digit: bool,
                                 use_special: bool) -> str:

        _result: GS = generate_password_string(
            password_length,
            use_digit,
            use_special,
            special_chars=SPECIAL_CHARS,
            min_password=PASS_MIN_LENGTH,
            max_password=PASS_MAX_LENGTH,
            message_value=MSG_VALUE_ERROR,
            message_type=MSG_TYPE_ERROR,
            message_unexpected=MSG_UNEXPECTED_ERROR,
            check_password_length=check_password_length,
            get_digits_list=get_char_list_digits,
            get_special_list=get_char_list_special,
            get_password_string=get_password_string,
        )

        if str != type(_result):
            raise ExceptionPassword(_result[1], _result[0])

        return _result


if __name__ == '__main__':
    _pass = ProcessorPassword.generate_password_string(24, use_digit=True, use_special=True)
    print(_pass)
