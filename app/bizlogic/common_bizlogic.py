
"""Common bizlogic
"""

from app.usrlib import image_utils, common
from app.models import *


def get_base_data(lang, request):
    """Make base data required on every page."""

    tags = [
        {
            'code' : tag_obj.code,
            'name' : common.dp_lang(lang, tag_obj.name_ja, tag_obj.name_en),
            'count': tag_obj.count,
        }
        for tag_obj in Tag.objects.filter(count__gt=0).order_by('id')
    ]
    years = [
        {
            'code' : year_obj.code,
            'count': year_obj.count,
        }
        for year_obj in Year.objects.filter(count__gt=0).order_by('id')
    ]

    return {
        'lang': lang,
        'page_title': get_site_name(lang),
        'site_desc' : get_site_desc(lang),
        'mainimage_fullpath': image_utils.get_default_mainimage(request),
        'tags': tags,
        'years': years,

    }


def get_site_name(lang):
    return common.dp_lang(lang, 'みろりHP', 'Mirori-HP')


def get_site_desc(lang):
    return common.dp_lang(lang,
        '★ 緑色さんの多目的ブログ みろりえいちぴー ごゆるりとおくつろぎあさーせ。 ★',
        '★ Midori\'s blog for multi-purposes. ★',
    )
