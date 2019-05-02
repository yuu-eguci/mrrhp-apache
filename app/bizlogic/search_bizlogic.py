
"""Search bizlogic
"""

from app.usrlib import common, consts
from app.models import *
from django.db.models import Q
from app.bizlogic import tag_bizlogic


def get_posts_by_search_words(lang, words):
    """Search posts by words."""
    if not words:
        return 0, []
    # When search words are 'a b c,' try to get posts that contain a, b and c all.
    posts = Post.available()
    for w in words:
        q = common.dp_lang(lang,
            Q(title_ja__contains=w) | Q(body_ja__contains=w) | Q(html__contains=w),
            Q(title_en__contains=w) | Q(body_en__contains=w) | Q(html__contains=w),
        )
        posts = posts.filter(q).order_by('publish_at').reverse()
    return len(posts), tag_bizlogic.__sort_by_year(lang, posts)
