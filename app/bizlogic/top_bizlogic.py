
"""Top bizlogic
"""

from app.models import *
from app.bizlogic import post_bizlogic
import random
from app.usrlib import consts


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


def get_recommended_posts(lang):
    """Get recommended posts set in DB."""

    # Recommended post codes.
    codes = (
        config_obj.value
        for config_obj
        in Config.objects.filter(key__startswith=consts.ConfigKeys.RECOMMENDED_POST_CODE)
    )

    # As want to pass not to append None, don't use comprehension(内包表記).
    posts = []
    for code in codes:
        post = Post.available().filter(code=code).first()
        if post:
            posts.append(post_bizlogic.format_post(post, lang, require_body=False))
    return posts
