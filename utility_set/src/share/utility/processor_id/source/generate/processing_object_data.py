from typing import TypeAlias, Type, Tuple, Any, List


T: TypeAlias = str | Tuple[str, Type[Exception]]


def processing_object_data(*args: Any,
                           base_message: str,
                           message_unexpected: str) -> T:

    base_message: str = f'{base_message} (processing object string)'

    try:
        if len(args) == 1:
            return str(args[0])

        _list_data: List[str] = []
        if len(args) > 1:
            for _arg in args:
                _list_data.append(str(_arg))

        return ' '.join(_list_data)

    except Exception as e:
        _message: str = message_unexpected.format(base_message, e)
        return _message, type(e)
