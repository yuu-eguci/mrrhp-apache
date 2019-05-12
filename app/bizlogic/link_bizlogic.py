
"""Link bizlogic
"""

from app.models import *
from app.bizlogic import post_bizlogic
from app.usrlib import common
import re


def register_all_posts_links():
    # Update all posts' links.

    for post_obj in Post.objects.all():
        register_link(post_obj)


def register_link(post_obj):
    """Register assigned post's links."""

    # Select body string for display.
    # Currently the priority is html > body_ja > body_en.
    # It is assumed that English body is always same as Japanese body.
    body = post_bizlogic.select_display_body(post_obj)

    # Get linked url's postcodes. As it shouldn't be duplicated, convert to set.
    codes = set(__get_linked_codes(body))
    if not codes:
        return

    # Get post objects by codes.
    linked_post_objs = __get_post_objs_with_404_check(codes, post_obj.code)

    # Register parent post and linked posts pairs.
    Link.objects.filter(parent_post=post_obj).delete()
    Link.objects.bulk_create(
        (
            Link(parent_post=post_obj, linked_post=p)
            for p in linked_post_objs
        )
    )


def __get_linked_codes(body:str) -> list:
    """From body string, get linked post codes."""

    return list(
        # Post code doesn't contain '/'.
        # What contains '/' is a link to page in the site other than post.
        filter(lambda _: '/' not in _, [
            # Don't forget to remove '#' link.
            # There is not post code having '#'.
            re.sub(r'href="/ja/|href="/en/|#.*?"|"', '', _)
            for _ in re.findall(r'href="/ja/.*?"|href="/en/.*?"', body)
        ])
    )


def __get_post_objs_with_404_check(codes:set, parent_code:str) -> list:
    """Get post objects by codes.
    This method sends notification when post object doesn't exist."""

    _ = []
    for code in codes:
        p = Post.available().filter(code=code).first()
        if not p:
            common.send_slack_notification(
                'There is link to non existing or non displaying page.'
                f' Link from: {parent_code}'
                f' Link to: {code}'
            )
            continue
        _.append(p)
    return _


def get_posts_having_linkto(post_obj, lang):
    """Select posts which have links to assigned post."""

    return [
        post_bizlogic.format_post(link.parent_post, lang, require_body=False)
        for link in Link.objects.filter(linked_post=post_obj)
    ]
