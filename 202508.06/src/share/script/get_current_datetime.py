from datetime import datetime


def get_current_datetime() -> str:

    from data import FMT_TIMESTAMP

    return datetime.now().strftime(format=FMT_TIMESTAMP)
