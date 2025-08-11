"""
Processing uuid: core model - generate uuid (folder)
Method: arguments_processing
"""

from typing import Any, Tuple, List


def arguments_processing_name_string(*args: Any,
                                     msg_unexpected_error: str) -> Tuple[bool, str, None | str]:
    """
    Method: argument "name_string" processing

    Args:
        *args (Any): processing data (list of different data type value(s))
        msg_unexpected_error (str): exception message

    Returns:
        Tuple[bool, str, str | None]:
            -   1 - operation succeeded (True) or failed (False)
            -   2 - operation result: processing data values if succeeded or exception message otherwise
            -   3 - additional data: None if succeeded or exception name otherwise
    """

    try:
        if len(args) == 1:
            _result: str = str(args[0])
            return True, _result, None

        _result: List[str] = []
        for _arg in args:
            _result.append(str(_arg))

        _result: str = ' '.join(_result)
        return True, _result, None

    except Exception as e:
        _message: str = msg_unexpected_error.format(':', e)
        return False, _message, type(e).__name__
