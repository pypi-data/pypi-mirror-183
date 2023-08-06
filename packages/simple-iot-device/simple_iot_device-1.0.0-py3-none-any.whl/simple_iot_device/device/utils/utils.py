import datetime
from datetime import timezone


def get_utc_time():
    return datetime.datetime.now(timezone.utc)


def get_utc_time_as_string():
    utc_time = datetime.datetime.now(timezone.utc)
    return utc_time.strftime("%Y-%m-%d %H:%M:%S.%f")


def get_utc_timestamp():
    utc_time = datetime.datetime.now(timezone.utc)
    return utc_time.timestamp()
