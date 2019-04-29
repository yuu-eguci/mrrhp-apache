from django.shortcuts import render, redirect
from app.usrlib import consts
import sys
from django.http import HttpResponse

def top(request, lang):
    data = {}
    return render(request, 'app/top.tpl', data)


def latest(request, lang):
    data = {}
    return render(request, 'app/post.tpl', data)


def post(request, lang, code):
    data = {}
    return render(request, 'app/post.tpl', data)


def search(request, lang):
    data = {}
    return render(request, 'app/list.tpl', data)


def tag(request, lang, code):
    data = {}
    return render(request, 'app/list.tpl', data)


def year(request, lang, code):
    data = {}
    return render(request, 'app/list.tpl', data)


def page_not_found(request, *args, **kw):
    return redirect('/')


def page_server_error(request, *args, **kw):

    # Write error info in /var/log/httpd/error_log
    # import traceback
    # print(traceback.format_exc())

    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponse(error_html)


def api_register_all_archive_posts(request):
    return HttpResponse('')
