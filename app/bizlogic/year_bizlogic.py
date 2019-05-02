
"""Year bizlogic
"""

from django.shortcuts import get_object_or_404
from app.models import *
from app.usrlib import consts, common
import pytz
from django.conf import settings
from django.utils import timezone


def get_year_obj_by_code(code):
    """Get one year by code. It occurs 404 when no year is found."""
    return get_object_or_404(Year, code=code)


def get_posts_by_month(lang, year_obj):
    """Get all posts belonging to assigned year and sort them by each month."""
    return __sort_by_month(lang, Post.available().filter(year=year_obj).order_by('publish_at').reverse())


def __sort_by_month(lang, post_objs):
    """Sort post objects by month."""

    posts_by_month = {}
    for p in post_objs:
        # TODO: Here change UTC time in DB to Japan time. But it may be better way to do this.
        p.publish_at = p.publish_at.astimezone(pytz.timezone(settings.TIME_ZONE))
        m = date_utils.format_by_lang_Ym(lang, p.publish_at)
        if m not in posts_by_month:
            posts_by_month[m] = []
        posts_by_month[m].append({
            'publish_at': date_utils.format_by_lang_Ymd(lang, p.publish_at),
            'code': p.code,
            'title': common.dp_lang(lang, p.title_ja, p.title_en),
            'tag': {
                'name': common.dp_lang(lang, p.tag.name_ja, p.tag.name_en),
                'code': p.tag.code,
            },
        })
    return posts_by_month
