from django.shortcuts import render
from app.usrlib import consts, common, image_utils, basic_auth
import sys
from django.http import HttpResponse
from app.bizlogic import (comment_bizlogic,
                          post_bizlogic,
                          tag_bizlogic,
                          year_bizlogic,
                          common_bizlogic,
                          search_bizlogic,
                          top_bizlogic,
                          link_bizlogic,
                         )
from django.conf import settings
from django.views.defaults import server_error as default_server_error


def top(request, lang):
    data = common_bizlogic.get_base_data(lang, request)
    data['is_top_page'] = True
    data['latest_posts'] = top_bizlogic.get_latest_posts(lang)
    data['pickup_post'] = top_bizlogic.get_pickup_post(lang)
    data['recently_updated_posts'] = top_bizlogic.get_recently_updated_posts(lang)
    data['recommended_posts'] = top_bizlogic.get_recommended_posts(lang)
    data['latest_year'] = data['latest_posts'][0]['publish_at'][:4] if data['latest_posts'] else ''
    return render(request, 'app/top.tpl', data)


def latest(request, lang):
    post_obj = post_bizlogic.get_latest_post_obj()
    if not post_obj:
        return page_not_found(request)
    formatted_post = post_bizlogic.format_post(post_obj, lang, require_body=True)
    related_formatted_posts, next_formatted_post, previous_formatted_post = post_bizlogic.get_related_formatted_posts(lang, post_obj)

    data = common_bizlogic.get_base_data(lang, request)
    data['is_latest_page'] = True
    data['page_title'] = f'{formatted_post["title"]} | {data["page_title"]}'
    data['post'] = formatted_post
    data['mainimage_fullpath'] = image_utils.get_mediafile_full_url(request, formatted_post['thumbnail']),
    data['comments'] = comment_bizlogic.get_comments_for_post(lang, post_obj)
    data['related_posts'] = related_formatted_posts
    data['next_post'] = next_formatted_post
    data['previous_post'] = previous_formatted_post
    return render(request, 'app/post.tpl', data)


def post(request, lang, code):
    post_obj = post_bizlogic.get_post_obj_by_code(code)
    if not post_obj:
        return page_not_found(request)

    # If viewer is allowed to see the unpublished post.
    if post_bizlogic.is_available_post_obj(post_obj):
        pass
    else:
        if not basic_auth.basic_auth(request):
            return basic_auth.http401()

    formatted_post = post_bizlogic.format_post(post_obj, lang, require_body=True)
    related_formatted_posts, next_formatted_post, previous_formatted_post = post_bizlogic.get_related_formatted_posts(lang, post_obj)

    data = common_bizlogic.get_base_data(lang, request)
    data['page_title'] = f'{formatted_post["title"]} | {data["page_title"]}'
    data['post'] = formatted_post
    data['mainimage_fullpath'] = image_utils.get_mediafile_full_url(request, formatted_post['thumbnail'])
    data['linked_from'] = link_bizlogic.get_posts_having_linkto(post_obj, lang)
    data['comments'] = comment_bizlogic.get_comments_for_post(lang, post_obj)
    data['related_posts'] = related_formatted_posts
    data['next_post'] = next_formatted_post
    data['previous_post'] = previous_formatted_post
    return render(request, 'app/post.tpl', data)


def search(request, lang):
    word = request.GET.get(key='s', default='')

    data = common_bizlogic.get_base_data(lang, request)
    data['is_search_page'] = True
    data['page_title'] = common.dp_lang(lang, '検索結果', 'Searching results') + f' | {data["page_title"]}'
    c, data['posts_dic'] = search_bizlogic.get_posts_by_search_words(lang, word)
    data['message'] = common.dp_lang(lang,
                                     f'{c}件見つかりました。',
                                     f'{c} posts were found.' if c > 1 else f'{c} post was found.')
    data['search_words'] = word
    return render(request, 'app/list.tpl', data)


def tag(request, lang, code):
    tag_obj = tag_bizlogic.get_tag_obj_by_code(code)

    data = common_bizlogic.get_base_data(lang, request)
    data['is_tag_page'] = True
    data['page_title'] = common.dp_lang(lang,
                                        tag_obj.name_ja + ' アーカイブ',
                                        tag_obj.name_en + ' Archives') + f' | {data["page_title"]}'
    data['posts_dic'] = tag_bizlogic.get_posts_by_year(lang, tag_obj)
    return render(request, 'app/list.tpl', data)


def year(request, lang, code):
    year_obj = year_bizlogic.get_year_obj_by_code(code)

    data = common_bizlogic.get_base_data(lang, request)
    data['is_year_page'] = True
    data['page_title'] = code + common.dp_lang(lang,
                                               ' アーカイブ',
                                               ' Archives') + f' | {data["page_title"]}'
    data['posts_dic'] = year_bizlogic.get_posts_by_month(lang, year_obj)
    return render(request, 'app/list.tpl', data)


def page_not_found(request, *args, **kw):
    data = common_bizlogic.get_base_data(consts.Lang.JA, request)
    data['is_404_page'] = True
    data['post'] = {
        'title': 'ページが見つかりません。',
        'body' : 'ヘッダのタグ一覧、年月一覧、検索欄から記事を探してみてください。',
    }
    return render(request, 'app/post.tpl', data)


def page_server_error(request, *args, **kw):

    # Write error info in /var/log/httpd/error_log
    import traceback
    # print(traceback.format_exc())

    # Send error info to Slack and display django default 500 page.
    common.send_slack_notification('\n'.join([
        'Server Error happened!',
        f'Request uri: {request.build_absolute_uri()}',
        f'HTTP_HOST: {request.META["HTTP_HOST"] if "HTTP_HOST" in request.META else "None"}',
        f'HTTP_REFERER: {request.META["HTTP_REFERER"] if "HTTP_REFERER" in request.META else "None"}',
        f'HTTP_USER_AGENT: {request.META["HTTP_USER_AGENT"] if "HTTP_USER_AGENT" in request.META else "None"}',
        f'QUERY_STRING: {request.META["QUERY_STRING"] if "QUERY_STRING" in request.META else "None"}',
        f'REMOTE_ADDR: {request.META["REMOTE_ADDR"] if "REMOTE_ADDR" in request.META else "None"}',
        f'REQUEST_METHOD: {request.META["REQUEST_METHOD"] if "REQUEST_METHOD" in request.META else "None"}',
        f'',
        traceback.format_exc(),
    ]))
    return default_server_error(request, *args, **kw)

    # Display 500 error page as if it is DEBUG=True env.
    # from django.views import debug
    # error_html = debug.technical_500_response(request, *sys.exc_info()).content
    # return HttpResponse(error_html)


def sitemap_posts(request):
    """Show all posts information as sitemap.xml format"""
    return HttpResponse(post_bizlogic.make_sitemap_posts_xml(), content_type='application/xml')
