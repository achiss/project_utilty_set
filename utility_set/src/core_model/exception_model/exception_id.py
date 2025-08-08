"""

"""

from typing import Type, Any

from src.core_model.exception_model._base_exception_model import BaseExceptionModel


class ExceptionID(BaseExceptionModel):
    __slots__ = ()

    def __init__(self, custom_type: Type[Any], exception_type: str, exception_message: str) -> None:
        super().__init__(custom_type.__name__, exception_type, exception_message)
