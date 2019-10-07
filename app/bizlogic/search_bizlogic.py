
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


def search_posts_by_get_query(request):
    """Search posts by GET queries and get them.
    t: Search title only.
    """

    # Get t key from GET query.
    keywords = set(
        filter(lambda t: t != '', request.GET.get(key='t', default='').split(' '))
    )

    # Get lang key from GET query.
    lang = request.GET.get(key='lang', default=consts.Lang.JA)

    # Search posts by the keywords.
    posts = __get_posts_by_search_words_title(lang, keywords)

    # Format posts, ramaining necessary information.
    formatted_posts = []
    for post in posts:
        # Change UTC time in DB to Japanese time.
        post.publish_at = date_utils.convert_timezone_to_local(post.publish_at)
        formatted_posts.append({
            'publish_at': date_utils.format_by_lang_Ymd(lang, post.publish_at),
            'code': post.code,
            'title': common.dp_lang(lang, post.title_ja, post.title_en),
            'tag': {
                'name': common.dp_lang(lang, post.tag.name_ja, post.tag.name_en),
                'code': post.tag.code,
            },
        })

    return formatted_posts


def __get_posts_by_search_words_title(lang, words):
    """Search title by words and get posts of search result."""
    if not words:
        return []
    # When search words are 'a b c', try to get posts that have title contains a, b and c all.
    q = Q()
    for w in words:
        # 'icontains' searches case insensitively.
        q &= common.dp_lang(lang, Q(title_ja__icontains=w), Q(title_en__icontains=w))
    return Post.available().filter(q).order_by('publish_at').reverse()
