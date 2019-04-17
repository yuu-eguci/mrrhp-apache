from django.shortcuts import render
from app.lib import consts
from app import views


# 言語振り分け。
def top_ja(request):
    return views.top(request, consts.Lang.JA)
def top_en(request):
    return views.top(request, consts.Lang.EN)
# def search_ja(request):
#     return search(request, consts.Lang.JA)
# def search_en(request):
#     return search(request, consts.Lang.EN)
# def tags_ja(request, code):
#     return tags(request, consts.Lang.JA, code)
# def tags_en(request, code):
#     return tags(request, consts.Lang.EN, code)
# def years_ja(request, code):
#     return years(request, consts.Lang.JA, code)
# def years_en(request, code):
#     return years(request, consts.Lang.EN, code)
# def post_ja(request, code):
#     return post(request, consts.Lang.JA, code)
# def post_en(request, code):
#     return post(request, consts.Lang.EN, code)
# def latest_ja(request):
#     return latest(request, consts.Lang.JA)
# def latest_en(request):
#     return latest(request, consts.Lang.EN)
