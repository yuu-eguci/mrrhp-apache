
"""Date utils
"""

import datetime
import os


def get_current_year() -> str:
    return datetime.datetime.now().strftime('%Y')


def get_current_microsecond() -> int:
    return datetime.datetime.now().microsecond
