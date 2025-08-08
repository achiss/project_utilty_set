from typing import Tuple, Any, Type


T: type[tuple] = Tuple[bool, str, Type[Exception] | None]


def processing_object_value(*args: Any) -> T: pass
