
"""Image bizlogic
"""

import os
from django.conf import settings
from app.usrlib import image_utils


def generate_thumbnail(imagename:str) -> None:
    """Create thumbnail from markdownx media folder to thumbnail media folder.
    If original file doesn't exist, just return None without any errors.
    """

    ORIGIN_PATH = os.path.join(settings.MEDIA_ROOT, 'markdownx', imagename)
    DEST_PATH   = os.path.join(settings.MEDIA_ROOT, 'thumbnail', imagename)

    # File doesn't exist -> nothing to do.
    # Try to use "PASS for boolean expression without NOT" I read from Readable Code.
    if os.path.isfile(ORIGIN_PATH):
        pass
    else:
        return

    # Create directory. exist_ok option was added from 3.2 version.
    os.makedirs(os.path.join(settings.MEDIA_ROOT, 'thumbnail'), exist_ok=True)

    # Create thumbnail image.
    image_utils.generate_thumbnail_360x195(ORIGIN_PATH, DEST_PATH)
