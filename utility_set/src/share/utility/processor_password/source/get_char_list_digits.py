from typing import List
from secrets import choice
from string import digits


def get_char_list_digits(value: int) -> List[str]:

    _result: int = 1 if value <= 14 else 2 if value <= 24 else 4
    _result: List[str] | None = [choice(digits) for _ in range(_result)]
    return _result
