from typing import Type
from datetime import date, time

from src.core_model.exception.base.base_exception_model import BaseExceptionModel


def exception_decorator(cls):

    class Wrapped(cls):
        __slots__ = ('__exception',)

        def __init__(self, original_exception_type: Type[Exception] | None, exception_message: str) -> None:
            self.__exception = BaseExceptionModel(
                custom_type=self.__class__,
                exception_type=original_exception_type,
                message=exception_message,
            )
            super().__init__(exception_message)

        @property
        def type(self) -> str: return self.__exception.custom_type.__name__

        @property
        def exception(self) -> str | None: return self.__exception.exception_type.__name__ if self.__exception.exception_type else None

        @property
        def message(self) -> str: return self.__exception.message

        @property
        def timestamp(self) -> str: return f'{self.__exception.datestamp} {self.__exception.timestamp}'

        @property
        def date(self) -> date: return self.__exception.datestamp

        @property
        def time(self) -> time: return self.__exception.timestamp

        def display(self) -> None:
            print(f'\nException description:'
                  f'\n- exception is error: {"True" if self.__exception.exception_type else "False"}')
            print(self.__exception)

    Wrapped.__name__ = cls.__name__
    return Wrapped
