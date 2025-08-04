""" BASE EXCEPTION MODEL """

from dataclasses import dataclass, field
from typing import TypeVar, Type, Any
from datetime import date, time

from src.share.script import get_current_date, get_current_time

T = TypeVar('T', bound='BaseExceptionModel')


@dataclass(frozen=True, slots=True)
class BaseExceptionModel:
    custom_type: Type[Any]
    exception_type: Type[Any] | None
    message: str
    datestamp: date = field(default_factory=get_current_date)
    timestamp: time = field(default_factory=get_current_time)

    # Class method
    @classmethod
    def create(cls: Type[Any], original_exception_type: Type[Any] | None, exception_message: str) -> T:
        return cls(
            custom_type=cls,
            exception_type=original_exception_type if original_exception_type else None,
            message=exception_message,
        )

    # Dunder methods
    def __str__(self) -> str:
        return (f'- model type: {self.custom_type.__name__}'
                f'\n- exception type: {self.exception_type.__name__ if self.exception_type else self.exception_type}'
                f'\n- message: {self.message}'
                f'\n- created as: {self.datestamp} {self.timestamp}')
