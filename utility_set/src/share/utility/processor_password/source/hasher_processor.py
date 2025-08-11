from typing import TypeAlias, Tuple, Type, Any

from bcrypt import gensalt, hashpw, checkpw

from data.settings import ITERATION_NUMBER, PREFIX_STRING, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH


T: TypeAlias = Tuple[bool, str, Type[Exception]] | Tuple[bool, bytes | bool]
Y: TypeAlias = bool | Tuple[str, Type[Exception]]


class HashingProcessor:
    __slots__ = ()

    #   VERIFY METHODS
    @staticmethod
    def __verify_password_string(value: Any,
                                 type_error: str,
                                 value_error: str) -> Y:

        if not isinstance(value, str):
            _message: str = type_error.format(
                'received password', 'str', type(value).__name__)
            return _message, TypeError

        if not (MIN_PASSWORD_LENGTH <= len(value) <= MAX_PASSWORD_LENGTH):
            _message: str = value_error.format(
                'received password length', f'should be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}')
            return _message, ValueError

        return True

    @staticmethod
    def __verify_password_hash(value: Any, fmt: bytes,
                               type_error: str,
                               value_error: str) -> Y:

        if not isinstance(value, bytes):
            _message: str = type_error.format(
                'received hashed password', 'bytes', type(value).__name__)
            return _message, TypeError

        if len(value) != 60 and value.startswith(fmt):
            _message: str = value_error.format('received hashed password', 'should be match the specified format')
            return _message, ValueError

        return False

    #   GENERATE SALT
    @staticmethod
    def __generate_salt(iteration: int, prefix: bytes) -> bytes: return gensalt(rounds=iteration, prefix=prefix)

    #   GET PASSWORD HASH
    @staticmethod
    def get_hash(password_string: str,
                 value_error: str, type_error: str, unexpected_error: str) -> T:

        try:
            if _check_result := HashingProcessor.__verify_password_string(
                    value=password_string, value_error=value_error, type_error=type_error)[0] is not True:
                return False, _check_result[0], _check_result[1]

            if _check_result := HashingProcessor.__generate_salt(
                    iteration=ITERATION_NUMBER, prefix=PREFIX_STRING)[0] is not True:
                return True, _check_result[0], _check_result[1]

            password_string: bytes = password_string.encode(encoding='utf-8')
            _result: bytes = hashpw(password=password_string, salt=_check_result[0])
            return True, _result

        except Exception as e:
            _message: str = unexpected_error.format('password hashing', e)
            return False, _message, type(e)

    #   VALIDATE PASSWORD HASH
    @staticmethod
    def verify_hash(password_string: str, hashed_password: bytes,
                    value_error: str, type_error: str, unexpected_error: str) -> T:

        try:
            if _check_result := HashingProcessor.__verify_password_string(
                    value=password_string, value_error=value_error, type_error=type_error)[0] is not True:
                return False, _check_result[0], _check_result[1]

            if _check_result := HashingProcessor.__verify_password_hash(
                    value=hashed_password, fmt=PREFIX_STRING, value_error=value_error, type_error=type_error)[0] is not True:
                return False, _check_result[0], _check_result[1]

            password_string: bytes = password_string.encode(encoding='utf-8')
            _result: bool = checkpw(password=password_string, hashed_password=hashed_password)
            return True, _result

        except Exception as e:
            _message: str = unexpected_error.format('hashed password verification', e)
            return False, _message, type(e)
