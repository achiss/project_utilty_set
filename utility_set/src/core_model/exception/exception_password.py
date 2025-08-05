""" EXCEPTION MODEL: PASSWORD """

from src.core_model.exception.base import exception_decorator


@exception_decorator
class ExceptionPassword(Exception):
    pass
