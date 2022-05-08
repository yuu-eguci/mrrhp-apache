
"""Methods used not in each page but on more global scope.
"""

from app.models import Config
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


def send_slack_notification(message: str):
    """When slack_webhook_url file doesn't exist, do nothing.
    Send message to slack_webhook_url."""

    if not settings.SLACK_WEBHOOK_URL:
        return

    # Send message.
    postman = create_postman(settings.SLACK_WEBHOOK_URL)
    postman.post(message)


def create_postman(webhook_url: str):
    """Create slack postman."""
    return slack_postman.SlackPostman(
        webhook_url,
        sender='Mrrhp System Info',
        sender_emoji=':snake:',
    )
