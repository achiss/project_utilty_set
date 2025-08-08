from datetime import datetime, time


def get_current_time_string() -> str:

    from data.conf import FMT_TIME_ISO

    return datetime.strftime(datetime.now(), format=FMT_TIME_ISO)


def get_current_time() -> time:

    c_time: datetime = datetime.now()
    c_time: time = time(c_time.hour, c_time.minute, c_time.second)
    return c_time
