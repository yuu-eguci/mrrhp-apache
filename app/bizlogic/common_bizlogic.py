
"""Common bizlogic
"""

from app.usrlib import image_utils, common
from app.models import *
from app.usrlib import consts


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
        for year_obj in Year.objects.filter(count__gt=0).order_by('id').reverse()
    ]

    return {
        'lang': lang,
        'page_title': get_site_name(lang),
        'site_desc' : get_site_desc(lang),
        'mainimage_fullpath': image_utils.get_default_mainimage(request),
        'tags': tags,
        'years': years,
        'site_version': get_version(lang),
    }


def get_site_name(lang):
    return common.dp_lang(lang, 'みろりHP', 'Mirori-HP')


def get_site_desc(lang):
    return common.dp_lang(lang,
        '★ 緑色さんの多目的ブログ みろりえいちぴー ごゆるりとおくつろぎあさーせ。 ★',
        '★ Midori\'s blog for multi-purposes. ★',
    )


def get_version(lang):
    version = Config.objects.filter(key=consts.ConfigKeys.SITE_VERSION).first()
    version = version.value if version else '3.0'
    print(version)
    return common.dp_lang(lang,
        f'みろりHP version {version}',
        f'Mirori-HP version {version}',
    )
