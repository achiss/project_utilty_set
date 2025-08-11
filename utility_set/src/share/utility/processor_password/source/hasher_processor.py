from typing import TypeAlias, Tuple, Type, Any

from bcrypt import gensalt, hashpw, checkpw

from data.settings import ITERATION_NUMBER, PREFIX_STRING, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH


T: TypeAlias = Tuple[bool, str, Type[Exception]] | Tuple[bool, bytes | bool]
Y: TypeAlias = bool | Tuple[str, Type[Exception]]


class HashingProcessor:
    __slots__ = ()

    #   VERIFY METHODS
    @staticmethod
    def __verify_password_string(value: Any) -> Y:
        if not isinstance(value, str):
            _message: str = f'password value should be a string, got {type(value).__name__}'
            return _message, TypeError

        if not (MIN_PASSWORD_LENGTH <= len(value) <= MAX_PASSWORD_LENGTH):
            _message: str = f'incorrect password length, should be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}'
            return _message, ValueError

        return True

    @staticmethod
    def __verify_password_hash(value: bytes, fmt: bytes) -> Y:
        if not isinstance(value, bytes):
            _message: str = f'hashed value should be a bytes, got {type(value).__name__}'
            return _message, TypeError

        if len(value) != 60 and value.startswith(fmt):
            _message: str = 'invalid hash format (library bcrypt)'
            return _message, ValueError

        return False

    #   GENERATE SALT
    @staticmethod
    def __generate_salt(iteration: int, prefix: bytes) -> bytes: return gensalt(rounds=iteration, prefix=prefix)

    #   GET PASSWORD HASH
    @staticmethod
    def get_hash(password_string: str) -> T:

        try:
            if (_check_result := HashingProcessor.__verify_password_string(value=password_string))[0] is not True:
                return False, _check_result[0], _check_result[1]

            _result: bytes = HashingProcessor.__generate_salt(iteration=12, prefix=b'2a')
            return True, _result

            password_string: bytes = password_string

        except Exception as e:
            _message: str = ''
            return False, _message, type(e)

    #   VALIDATE PASSWORD HASH
    @staticmethod
    def verify_hash(password_string: str, hashed_password: bytes) -> T:

        try:
            if (_check_result := HashingProcessor.__verify_password_string(value=password_string))[0] is not True:
                return False, _check_result[0], _check_result[1]

            if (_check_result := HashingProcessor.__verify_password_hash(value=hashed_password, fmt=b'2a'))[0] is not True:
                return False, _check_result[0], _check_result[1]

            password_string: bytes = password_string.encode(encoding='utf-8')
            _result: bool = checkpw(password=password_string, hashed_password=hashed_password)
            return True, _result

        except Exception as e:
            _message: str = ''
            return False, _message, type(e)
