from typing import List
from secrets import choice


def get_char_list_special(value: int, special_chars: str) -> List[str] | None:

    _result: int = 1 if value <= 14 else 2 if value <= 24 else 3
    _result: List[str] | None = [choice(special_chars) for _ in range(_result)]
    return _result
