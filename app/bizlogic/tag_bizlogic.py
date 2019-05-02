
"""Tag bizlogic
"""

from django.shortcuts import get_object_or_404
from app.models import *
from app.usrlib import consts, common
import pytz
from django.conf import settings
from django.utils import timezone
from bulk_update.helper import bulk_update
from django.db.models import Q, Count


def get_tag_obj_by_code(code):
    """Get one tag by code. It occurs 404 when no tag is found."""
    return get_object_or_404(Tag, code=code)


def get_posts_by_year(lang, tag_obj):
    """Get all posts belonging to assigned tag and sort them by each year."""
    return __sort_by_year(lang, Post.available().filter(tag=tag_obj).order_by('publish_at').reverse())


def __sort_by_year(lang, post_objs):
    """Sort post objects by year."""

    posts_by_year = {}
    for p in post_objs:
        y = p.year.code
        if y not in posts_by_year:
            posts_by_year[y] = []
        # TODO: Here change UTC time in DB to Japan time. But it may be better way to do this.
        p.publish_at = p.publish_at.astimezone(pytz.timezone(settings.TIME_ZONE))
        posts_by_year[y].append({
            'publish_at': date_utils.format_by_lang_Ymd(lang, p.publish_at),
            'code': p.code,
            'title': common.dp_lang(lang, p.title_ja, p.title_en),
            'tag': {
                'name': common.dp_lang(lang, p.tag.name_ja, p.tag.name_en),
                'code': p.tag.code,
            },
        })
    return posts_by_year


def update_count():
    """Update count column."""

    # Set all records zero.
    Tag.objects.update(count=0)

    # Update count.
    tag_objs = [
        Tag(id=c['tag_id'], count=c['count'])
        for c in Post.available().values('tag_id').annotate(count=Count('tag_id'))
    ]
    bulk_update(tag_objs, update_fields=['count'])
