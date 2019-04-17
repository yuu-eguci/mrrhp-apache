from django.shortcuts import render
from app.lib import consts

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
