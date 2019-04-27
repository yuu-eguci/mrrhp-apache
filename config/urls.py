"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views, views_lang
from django.conf.urls import handler404, handler500
from app.usrlib import common

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views_lang.top_ja),
    path('ja/', views_lang.top_ja),
    path('en/', views_lang.top_en),
    path('ja/latest/', views_lang.latest_ja),
    path('en/latest/', views_lang.latest_en),
    path('ja/<str:code>', views_lang.post_ja),
    path('en/<str:code>', views_lang.post_en),
    path('ja/search/', views_lang.search_ja),
    path('en/search/', views_lang.search_en),
    path('ja/tags/<str:code>', views_lang.tag_ja),
    path('en/tags/<str:code>', views_lang.tag_en),
    path('ja/years/<str:code>', views_lang.year_ja),
    path('en/years/<str:code>', views_lang.year_en),
    path('markdownx/', include('markdownx.urls')),
]

handler404 = views.page_not_found

# TODO: You have to comment out this on the real production env.
# Without comment out, it displays 500 error even on Apache env.
handler500 = views.page_server_error
