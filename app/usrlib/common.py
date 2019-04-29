
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
