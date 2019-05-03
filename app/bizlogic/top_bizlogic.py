
"""Top bizlogic
"""

from app.models import *
from app.bizlogic import post_bizlogic
import random


def get_latest_posts(lang):
    """Get 5 latest posts."""
    return (
        post_bizlogic.format_post(post_obj, lang, require_body=False)
        for post_obj in Post.available().order_by('publish_at').reverse()[:5]
    )


def get_pickup_post(lang):
    """Randomly pick one post up, from newer posts."""
    picknum = random.randint(1, Post.available().count()/2)
    return post_bizlogic.format_post(
        Post.available().order_by('publish_at').reverse()[picknum:picknum+1].first(),
        lang,
        require_body=False,
    )


def get_recently_updated_posts(lang):
    """Get 5 recently updated posts."""
    return (
        post_bizlogic.format_post(post_obj, lang, require_body=False)
        for post_obj in Post.available().order_by('updated_at').reverse()[:5]
    )
