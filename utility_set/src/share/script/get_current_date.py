from datetime import datetime, date


def get_current_date_string() -> str:

    from data.conf import FMT_DATE_ISO

    return datetime.strftime(datetime.now(), format=FMT_DATE_ISO)


def get_current_date() -> date:

    c_date: datetime = datetime.now()
    c_date: date = date(c_date.year, c_date.month, c_date.day)
    return c_date
