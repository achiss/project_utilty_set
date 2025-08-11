from typing import TypeAlias, Tuple, Type, Any, List

T: TypeAlias = Tuple[bool, str, Type[Exception] | None]


def processing_object_data(*args: Any) -> 'T':

    from data.message import MESSAGE_UNEXPECTED_ERROR

    _func_message: str = 'arg(s) processing "object data" for uuid5 generation'

    try:
        if len(args) == 1:
            _object: str = str(args[0])
            return True, _object, None

        _objects_list: List[str] = []
        for _arg in args:
            _objects_list.append(str(_arg))

        _objects_list: str = ' '.join(_objects_list)
        return True, _objects_list, None

    except Exception as e:
        _message: str = MESSAGE_UNEXPECTED_ERROR.format(_func_message, e)
        return False, _message, type(e)
