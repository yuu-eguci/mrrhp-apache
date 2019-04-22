
"""Methods used not in each page but on more global scope.
"""

from app.models import *


def _get_config_value(key):
    """Get value of Config model by key."""
    row = Config.objects.filter(key=key).first()
    if not row:
        return False
    return row.value
