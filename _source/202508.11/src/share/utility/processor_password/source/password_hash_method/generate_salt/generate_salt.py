from typing import TypeAlias, Tuple, Type

from bcrypt import gensalt

from src.share.utility.processor_password.source.password_hash_method.generate_salt.verify_iteration_number import \
    verify_iteration_number
from src.share.utility.processor_password.source.password_hash_method.generate_salt.verify_prefix import \
    verify_prefix

T: TypeAlias = Tuple[bool, bytes | str, Type[Exception] | None]


def generate_salt(iteration_number: int, prefix: bytes) -> 'T':
    """
    """

    if not (_result := verify_iteration_number(iteration_number))[0]:
        return False, _result[1], ValueError

    if not (_result := verify_prefix(prefix))[0]:
        return False, _result[1], ValueError

    try:
        _result: bytes = gensalt(rounds=iteration_number, prefix=prefix)
        return True, _result, None

    except Exception as e:
        _message: str = ''
        return False, _message, type(e)
