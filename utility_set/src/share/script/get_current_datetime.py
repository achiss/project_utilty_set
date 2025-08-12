from datetime import datetime


def get_current_datetime() -> str:

    from data.settings import FMT_DATETIME

    return datetime.now().strftime(format=FMT_DATETIME)
