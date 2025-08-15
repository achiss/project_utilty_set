from pathlib import Path
from typing import TypeAlias, Type, Tuple


T: TypeAlias = bool | Tuple[str, Type[Exception]]


def file_create(value: Path) -> T:

    try:
        with value.open('w') as _:
            pass

        return True

    except FileNotFoundError as e:
        pass

    except PermissionError as e:
        pass

    except Exception as e:
        pass
