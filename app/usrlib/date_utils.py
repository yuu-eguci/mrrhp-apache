
"""Date utils
"""

import datetime


def get_current_year() -> str:
    return datetime.datetime.now().strftime('%Y')
