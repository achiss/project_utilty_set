""" BASE EXCEPTION MODEL """

from dataclasses import dataclass, field

from src.share.script import get_current_datetime


@dataclass(frozen=True, slots=True)
class BaseExceptionModel:
    custom_type: str
    exception_type: str | None
    message: str
    created_as: str = field(default_factory=get_current_datetime)

    # Dunder methods
    def __str__(self) -> str:
        return (f'- class type: {self.custom_type}\n'
                f'- exception type: {self.exception_type}\n'
                f'- message: {self.message}\n'
                f'- created as: {self.created_as}\n')
