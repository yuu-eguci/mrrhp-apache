
"""Date utils
"""

import datetime
from app.usrlib import common
import pytz
from django.conf import settings


def get_current_year() -> str:
    return datetime.datetime.now().strftime('%Y')


def get_current_microsecond() -> int:
    return datetime.datetime.now().microsecond


def format_by_lang_YmdHM(lang, date):
    """Ymd HM format by lang."""
    return datetime.datetime.strftime(
        date,
        common.dp_lang(lang, '%Y-%m-%d %H:%M', '%b %d, %Y %H:%M')
    )


def format_by_lang_Ymd(lang, date):
    """Ymd format by lang."""
    return datetime.datetime.strftime(
        date,
        common.dp_lang(lang, '%Y-%m-%d', '%b %d, %Y')
    )


def format_by_lang_Ym(lang, date):
    """Ym format by lang."""
    return datetime.datetime.strftime(
        date,
        common.dp_lang(lang, '%Y/%m', '%b %Y')
    )


def format_by_lang_md(lang, date):
    """md format by lang."""
    return datetime.datetime.strftime(
        date,
        common.dp_lang(lang, '%m/%d', '%b %d')
    )


def format_iso(date):
    """Representation of dates and times is
    an international standard coveringthe exchange of date- and time-related data."""
    return date.isoformat()


def convert_timezone_to_local(dt):
    """Convert datetime tzinfo to local."""
    return dt.astimezone(pytz.timezone(settings.TIME_ZONE))


def set_timezone_local(dt):
    """Add native datetimeobject tzinfo converting to aware object."""
    return pytz.timezone(settings.TIME_ZONE).localize(dt)


def get_current_year_id():
    """Get id for current year of Year model.
    It should be got from DB. But it doesn't work before migrate."""
    return {
        2006: 1,
        2007: 2,
        2008: 3,
        2009: 4,
        2010: 5,
        2011: 6,
        2012: 7,
        2013: 8,
        2014: 9,
        2015: 10,
        2016: 11,
        2017: 12,
        2018: 13,
        2019: 14,
        2020: 15,
        2021: 16,
        2022: 17,
        2023: 18,
        2024: 19,
        2025: 20,
        2026: 21,
        2027: 22,
        2028: 23,
        2029: 24,
        2030: 25,
        2031: 26,
        2032: 27,
        2033: 28,
        2034: 29,
        2035: 30,
        2036: 31,
        2037: 32,
        2038: 33,
        2039: 34,
        2040: 35,
        2041: 36,
        2042: 37,
        2043: 38,
        2044: 39,
        2045: 40,
    }[int(get_current_year())]


def get_ago_label(lang, dt):
    """
    Convert specified datetime into a string, '*** days,months,years ago.'
    As conversion rule is made depending on creator's sense, it is sometimes different from yours.
    HACK: It's hard to read and has a room to be shortened.
    """

    now = set_timezone_local(datetime.datetime.now())
    years = now.year - dt.year
    months = now.month - dt.month
    days = now.day - dt.day
    actual_days = (now - dt).days

    if actual_days == 0:
        return common.dp_lang(lang, '今日', 'Today')

    before_today_of_each_year = months >= 0 and days >= 0
    if not before_today_of_each_year:
        years -= 1

    before_today_of_each_month = days >= 0
    if not before_today_of_each_month:
        months = 11 if months == 0 else months - 1

    labels = common.dp_lang(
        lang,
        ['年前', 'ヶ月前', '日前'],
        [' years ago', ' months ago', ' days ago'],
    )
    for num, label in zip([years, months, actual_days], labels):
        if num > 0:
            label = label.replace('s', '') if num == 1 else label
            return f'{num}{label}'
