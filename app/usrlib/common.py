
"""Methods used not in each page but on more global scope.
"""

from app.models import *
import os
from app.usrlib import consts, slack_postman
import markdown
from django.conf import settings


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


def send_slack_notification(message:str):
    """When slack_webhook_url file doesn't exist, do nothing.
    Send message to slack_webhook_url."""

    # Get slack_webhook_url.
    webhook_url_file = os.path.join(settings.BASE_DIR, 'slack_webhook_url')
    if not os.path.exists(webhook_url_file):
        return
    with open(webhook_url_file, 'r', encoding=consts.Encoding.UTF8) as f:
        webhook_url = f.read()

    # Send message.
    postman = create_postman(webhook_url)
    postman.post(message)


def create_postman(webhook_url:str):
    """Create slack postman."""
    return slack_postman.SlackPostman(
        webhook_url,
        sender='Mrrhp System Info',
        sender_emoji=':snake:',
    )
