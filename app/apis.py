
from app.usrlib import basic_auth
from django.http import HttpResponse
from app.bizlogic import (archive_bizlogic,
                          image_bizlogic,
                          comment_bizlogic,
                          link_bizlogic,
                          search_bizlogic,
                         )
from django.http.response import JsonResponse


def __exec_api(request, api_func):
    """After basic authentication, execute assigned method."""

    if not basic_auth.basic_auth(request):
        return basic_auth.http401()
    api_func()
    return HttpResponse('')


def api_register_all_archive_posts(request):
    return __exec_api(request, archive_bizlogic.register_all_archive_posts)


def api_organize_thumbnail(request):
    return __exec_api(request, image_bizlogic.organize_thumbnail)


def api_organize_media(request):
    return __exec_api(request, image_bizlogic.organize_media)


def api_register_comments(request):
    return __exec_api(request, comment_bizlogic.register_comment_from_pickle)


def api_register_links(request):
    return __exec_api(request, link_bizlogic.register_all_posts_links)


def api_search_posts(request):
    """Search and get posts by GET queries and return them as Json format.
    t   : keywords, used to search title
    lang: ja or en
    """
    return JsonResponse({'posts':search_bizlogic.search_posts_by_get_query(request)})
