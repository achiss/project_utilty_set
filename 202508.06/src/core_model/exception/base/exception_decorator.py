""" BASE EXCEPTION MODEL DECORATOR """

from typing import Type

from src.core_model.exception.base.base_exception_model import BaseExceptionModel


def exception_decorator(cls):

    class Wrapped(cls):
        __slots__ = ('__exception',)

        def __init__(self, original_exception_type: Type[Exception] | None, exception_message: str) -> None:
            self.__exception = BaseExceptionModel(
                custom_type=self.__class__.__name__,
                exception_type=original_exception_type.__name__ if original_exception_type else None,
                message=exception_message,
            )
            super().__init__(exception_message)

        @property
        def type(self) -> str: return self.__exception.custom_type

        @property
        def exception(self) -> str | None: return self.__exception.exception_type

        @property
        def message(self) -> str: return self.__exception.message

        @property
        def timestamp(self) -> str: return self.__exception.created_as

        def display(self) -> None:
            print(f'\nException description:'
                  f'\n- exception as error: {"True" if self.__exception.exception_type else "False"}')
            print(self.__exception)

    Wrapped.__name__ = cls.__name__

    return Wrapped
