from src.share.utility.processor_password.source.hasher_processor import HashingProcessor as HashMethod
from data.message import MSG_TYPE_ERROR, MSG_VALUE_ERROR, MSG_UNEXPECTED_ERROR


class ProcessorPassword:
    __slots__ = ()

    @staticmethod
    def get_hash(password_string: str) -> bytes:
        if _result := HashMethod.get_hash(
                password_string, MSG_VALUE_ERROR, MSG_TYPE_ERROR, MSG_UNEXPECTED_ERROR) is False:
            raise type(_result[2])(_result[1])

        return _result[1]

    @staticmethod
    def verify_hash(password_string: str, hashed_password: bytes) -> bool: pass
