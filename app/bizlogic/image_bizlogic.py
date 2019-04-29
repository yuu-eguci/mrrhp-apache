
"""Image bizlogic
"""

import os
from django.conf import settings
from app.usrlib import image_utils
from app.models import *
import re


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


def organize_thumbnail():
    """Remove duplicated thumbnails."""

    existing_thumbnails = os.listdir(os.path.join(settings.MEDIA_ROOT, 'thumbnail'))
    required_thumbnails = [post['thumbnail'] for post in Post.objects.values('thumbnail')]
    for unrequired_thumbnail in set(existing_thumbnails) - set(required_thumbnails):
        os.remove(os.path.join(settings.MEDIA_ROOT, 'thumbnail', unrequired_thumbnail))


def organize_media():
    """Remove duplicated media files."""

    existing_mediafiles = os.listdir(os.path.join(settings.MEDIA_ROOT, 'markdownx'))
    required_mediafiles = __extract_valid_mediafilenames()
    for unrequired_thumbnail in set(existing_mediafiles) - set(required_mediafiles):
        os.remove(os.path.join(settings.MEDIA_ROOT, 'markdownx', unrequired_thumbnail))


def __extract_valid_mediafilenames():
    """Gather all media file basenames which are contained in Post model."""

    basenames = set()
    for post in Post.objects.all():
        search_target = post.body_ja + post.body_en + post.html
        reg = r'/media/markdownx/.*?.jpg|/media/markdownx/.*?.png|/media/markdownx/.*?.gif'
        for basename in map(os.path.basename, re.findall(reg, search_target)):
            basenames.add(basename)
    return basenames
