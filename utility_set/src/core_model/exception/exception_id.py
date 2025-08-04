from src.core_model.exception.base import exception_decorator


@exception_decorator
class ExceptionId(Exception):
    pass


if __name__ == '__main__':
    _ex = ExceptionId(None, 'Test message')
    _ex.display()
    print(_ex.type)
