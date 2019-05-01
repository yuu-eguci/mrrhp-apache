
"""Methods used not in each page but on more global scope.
"""

from app.models import *
import os
from app.usrlib import consts
import markdown


def _get_config_value(key):
    """Get value of Config model by key."""
    row = Config.objects.filter(key=key).first()
    if not row:
        return False
    return row.value


def read_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding=consts.Encoding.UTF8) as f:
            return f.read()
    return ''


def get_markdown_metadata(filepath):
    md = markdown.Markdown(extensions=['meta'])
    md.convert(read_file(filepath))
    return md.Meta


def dp_lang(lang, for_ja, for_en):
    """Depends on lang.
    As Japanese is default, it return for_ja when for_en variable is empty.
    """
    if not for_en:
        return for_ja
    return for_ja if lang == consts.Lang.JA else for_en


def get_site_name(lang):
    return dp_lang(lang, 'みろりHP', 'Mirori-HP')


def get_site_desc(lang):
    return dp_lang(lang,
        '★ 緑色さんの多目的ブログ みろりえいちぴー ごゆるりとおくつろぎあさーせ。 ★',
        '★ Midori\'s blog for multi-purposes. ★',
    )

