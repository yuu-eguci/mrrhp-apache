from django.shortcuts import redirect
from app.usrlib import consts
from app import views


# Depends on language.
def top(request):
    return redirect(f'/{consts.Lang.JA}/')


def top_ja(request):
    return views.top(request, consts.Lang.JA)


def top_en(request):
    return views.top(request, consts.Lang.EN)


def latest_ja(request):
    return views.latest(request, consts.Lang.JA)


def latest_en(request):
    return views.latest(request, consts.Lang.EN)


def post_ja(request, code):
    return views.post(request, consts.Lang.JA, code)


def post_en(request, code):
    return views.post(request, consts.Lang.EN, code)


def search_ja(request):
    return views.search(request, consts.Lang.JA)


def search_en(request):
    return views.search(request, consts.Lang.EN)


def tag_ja(request, code):
    return views.tag(request, consts.Lang.JA, code)


def tag_en(request, code):
    return views.tag(request, consts.Lang.EN, code)


def year_ja(request, code):
    return views.year(request, consts.Lang.JA, code)


def year_en(request, code):
    return views.year(request, consts.Lang.EN, code)
