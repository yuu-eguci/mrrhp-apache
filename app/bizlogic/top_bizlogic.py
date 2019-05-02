
"""Top bizlogic
"""

from app.models import *
from app.bizlogic import post_bizlogic


def get_latest_posts(lang):
    """Get 5 latest posts."""
    return (
        post_bizlogic.format_post(post_obj, lang, require_body=False)
        for post_obj in Post.available().order_by('publish_at').reverse()[:5]
    )
