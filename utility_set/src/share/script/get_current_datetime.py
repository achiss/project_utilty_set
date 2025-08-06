"""
Script: get current datetime
"""

from datetime import datetime


def get_current_datetime() -> str:

    from data.cfg import FMT_DATETIME

    return datetime.now().strftime(format=FMT_DATETIME)
