
"""Methods used not in each page but on more global scope.
"""

from app.models import *
from app.usrlib import consts


def _get_config_value(key):
    """Get value of Config model by key."""
    row = Config.objects.filter(key=key).first()
    if not row:
        return False
    return row.value


def enable_show_500_error():
    return _get_config_value(consts.ConfigKeys.SHOW_500_ERROR) == '1'
