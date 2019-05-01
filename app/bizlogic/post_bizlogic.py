
"""Post bizlogic
"""

from django.shortcuts import get_object_or_404
from app.models import *
from app.usrlib import consts, common
import pytz
from django.conf import settings


def __get_post_by_code(code):
    """Get one post by code. It occurs 404 when no post is found."""
    return get_object_or_404(
        Post,
        code=code,
        publish_at__lte=datetime.datetime.today(),
    )


def get_post(code, lang, require_body=False):
    """Get one post by code. It occurs 404 when no post is found.
    This method organizes post data for display on tpl file.
    """

    post = __get_post_by_code(code)
    
    # TODO: Here change UTC time in DB to Japan time. But it may be better way to do this.
    post.publish_at = post.publish_at.astimezone(pytz.timezone(settings.TIME_ZONE))

    return {
        'title'     : common.dp_lang(lang, post.title_ja, post.title_en),     # Depends on lang
        'code'      : post.code,                                              # As it is
        'publish_at': date_utils.format_by_lang_Ymd(lang, post.publish_at),   # Change format depends on lang
        'thumbnail' : post.thumbnail,                                         # As it is
        'body'      : common.dp_lang(lang,                                    # Change markdown text to html
                                     post.get_markdownified_body_ja(),
                                     post.get_markdownified_body_en())
                      if require_body else '',
        'tag'       : {                                                       # As it is.
            'name': common.dp_lang(lang, post.tag.name_ja, post.tag.name_en),
            'code': post.tag.code,
        },
        'no_en_version': not post.body_en,                                    # If has English body
        # TODO: Make archive datetime aware and this line available.
        # 'is_before2018': date_utils.is_before_2018(post.publish_at),
    }
