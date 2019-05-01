
"""Comment bizlogic
"""

import os
from django.conf import settings
from app.models import *
import pickle
import pytz
from app.usrlib import date_utils


def register_comment_from_pickle() -> None:
    """Extract data from pickle and register comment to DB."""

    # It is supposed that this method will be called only once.
    # Delete all comments at first.
    Comment.objects.all().delete()

    # Extract data from pickle.
    with open(os.path.join(settings.BASE_DIR, '__drafts', 'comments.pickle'), 'rb') as f:
        data = pickle.load(f)

    # Register comments.
    Comment.objects.bulk_create(__create_commen_objs_as_iter(data))


def __create_commen_objs_as_iter(data:dict):
    """Create Comment objects from comment data dict and yield them."""
    for postcode, comments_data in data.items():
        post = Post.objects.filter(code=postcode).first()
        for comment_data in comments_data:
            yield Comment(
                post=post,
                # TODO: Add timezone info. It may be refactored.
                comment_at=pytz.timezone(settings.TIME_ZONE).localize(comment_data['date']),
                name=comment_data['name'],
                body=comment_data['desc'])


def get_comments_for_post(lang, post_obj):
    """Get comment for assigned post."""
    return [
        {
            # TODO: Here change UTC time in DB to Japan time. But it may be better way to do this.
            'comment_at': comment.comment_at.astimezone(pytz.timezone(settings.TIME_ZONE)),
            'name'      : comment.name,
            'body'      : comment.body,
        }
        for comment in Comment.objects.filter(post=post_obj).order_by('comment_at')
    ]
