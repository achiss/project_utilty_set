from typing import TypeAlias, Type, Tuple, Callable, List


T: TypeAlias = str | Tuple[str, Type[Exception]]

_base_message: str = 'generating password'


def generate_password_string(length_value: int,
                             use_digit: bool,
                             use_special: bool,
                             special_chars: str,
                             min_password: int,
                             max_password: int,
                             message_value: str,
                             message_unexpected: str,
                             get_digits_list: Callable,
                             get_special_list: Callable,
                             get_password_string: Callable) -> T:

    if min_password > length_value > max_password:
        _message: str = message_value.format(
            _base_message, f'password length should be between {min_password} and {max_password}')
        return _message, ValueError

    _password_parts: List[str] = []
    if use_digit:
        _digit_list: List[str] = get_digits_list(length_value)
        _password_parts.extend(_digit_list)

    if use_special:
        _special_list: List[str] = get_special_list(length_value, special_chars)
        _password_parts.extend(_special_list)

    _received_data: T = get_password_string(length_value, _password_parts, _base_message, message_unexpected)
    if str != type(_received_data):
        return _received_data

    return _received_data
