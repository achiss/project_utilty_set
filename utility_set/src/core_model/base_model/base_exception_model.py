from typing import Type

from src.core_model.data_model import StructExceptionModel


class BaseExceptionModel(Exception):
    __slots__ = ('__data',)

    def __init__(self, original_exception: Type[Exception], exception_message: str | None) -> None:
        self.__data = self.__create(self.__class__, original_exception, exception_message)

    @classmethod
    def __create(cls,
                 custom_type: Type[object],
                 original_exception: Type[Exception],
                 exception_message: str | None) -> 'StructExceptionModel':

        from src.share.script import get_current_datetime

        return StructExceptionModel(
            custom_exception=custom_type.__name__,
            original_exception=original_exception.__name__ if original_exception else None,
            message=exception_message,
            timestamp=get_current_datetime()
        )

    @property
    def custom_type(self) -> str: return self.__data.custom_exception

    @property
    def original_type(self) -> str | None: return self.__data.original_exception

    @property
    def message(self) -> str: return self.__data.message

    @property
    def timestamp(self) -> str: return self.__data.timestamp

    def display(self) -> None: print(self.__data)

    def __str__(self) -> str: return self.__data.__str__()
