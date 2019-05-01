
"""Date utils
"""

import datetime
import os
from app.usrlib import common


def get_current_year() -> str:
    return datetime.datetime.now().strftime('%Y')


def get_current_microsecond() -> int:
    return datetime.datetime.now().microsecond


def format_by_lang_YmdHM(lang, date):
    """Ymd HM format by lang."""
    return datetime.datetime.strftime(date,
        common.dp_lang(lang, '%Y-%m-%d %H:%M', '%b %d, %Y %H:%M'))


def format_by_lang_Ymd(lang, date):
    """Ymd format by lang."""
    return datetime.datetime.strftime(date,
        common.dp_lang(lang, '%Y-%m-%d', '%b %d, %Y'))


def format_by_lang_Ym(lang, date):
    """Ym format by lang."""
    return datetime.datetime.strftime(date,
        common.dp_lang(lang, '%Y/%m', '%b %Y'))


def format_by_lang_md(lang, date):
    """md format by lang."""
    return datetime.datetime.strftime(date,
        common.dp_lang(lang, '%m/%d', '%b %d'))


def is_before_2018(date):
    """Returns if this date is before 2018.01.01"""
    print(date, datetime.datetime(2019, 1, 1))
    return date < datetime.datetime(2019, 1, 1)
