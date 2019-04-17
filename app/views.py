from django.shortcuts import render
from app.lib import consts

def top(request, lang):
    data = {}
    return render(request, 'app/top.tpl', data)
