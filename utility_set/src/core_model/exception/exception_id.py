""" EXCEPTION MODEL: ID """

from src.core_model.exception.base import exception_decorator


@exception_decorator
class ExceptionId(Exception):
    pass
