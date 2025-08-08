"""
BASE EXCEPTION MODEL
"""

from dataclasses import dataclass, field

from src.share.script import get_current_datetime


@dataclass(frozen=True, slots=True)
class BaseExceptionModel(Exception):
    custom_type: str
    exception_type: str | None
    message: str
    created_as: str = field(default_factory=get_current_datetime)

    def display(self) -> None: print(self.__str__())

    # Dunder methods
    def __str__(self) -> str:
        return (f'\n- class type: {self.custom_type}'
                f'\n- exception type: {self.exception_type}'
                f'\n- message: {self.message}'
                f'\n- created as: {self.created_as}')
