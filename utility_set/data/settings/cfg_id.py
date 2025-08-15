from re import compile
from re import Pattern, IGNORECASE


#   PATTERS
REGEX_UUID: Pattern = compile(
    pattern=r'^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
    flags=IGNORECASE
)

REGEX_UUID4: Pattern = compile(
    pattern=r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
    flags=IGNORECASE
)

REGEX_UUID5: Pattern = compile(
    pattern=r'^[a-f0-9]{8}-[a-f0-9]{4}-5[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
    flags=IGNORECASE
)


#   CONST
CHARS_NUMBER_UUID: int = 36
