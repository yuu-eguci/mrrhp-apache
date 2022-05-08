
"""Image utils
"""

from PIL import Image
import os
from app.usrlib import date_utils
import hashlib


def generate_thumbnail_360x195(origin_path, dest_path, quality=70):
    """Resize image to 360x195.
    As horizontal direction precedes, vertical direction is possible to get white spaces."""

    pil_origin = Image.open(origin_path)
    w, h = pil_origin.size

    # Width 360px
    resize_rate = 360 / w
    pil_w360 = pil_origin.resize((int(w * resize_rate), int(h * resize_rate)))
    w, h = pil_w360.size

    # 360x195。
    bg = Image.new('RGB', [360, 195], (255, 255, 255))
    bg.paste(pil_w360, (0, int((195 - h) / 2)))

    bg.save(dest_path, quality=quality)


# Get image basenames from the specified directory.
def get_image_basenames(dirpath) -> iter:
    return filter(lambda _: os.path.splitext(_)[-1] in ['.jpg', '.gif', '.png'],
                  os.listdir(dirpath))


# Create unique name for image. You'll get unique name in the directory specified as unique_at.
def get_unique_image_name(original_basename, unique_at):
    will_be_hashed = original_basename + str(date_utils.get_current_microsecond())
    ext = os.path.splitext(original_basename)[-1]
    new_name = hashlib.md5((will_be_hashed).encode('utf8')).hexdigest() + ext
    if new_name in os.listdir(unique_at):
        return get_unique_image_name(original_basename, unique_at)
    return new_name


def get_mediafile_full_url(request, basename):
    """Depends on env, returns mediafile full path."""
    return f'{request.scheme}://{request.get_host()}/media/markdownx/{basename}'


def get_default_mainimage(request):
    """Returns default mainimage."""
    return f'{request.scheme}://{request.get_host()}/static/app/img/core/blog-img-size.jpg'
