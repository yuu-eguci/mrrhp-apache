
"""Image utils
"""

from PIL import Image


def generate_thumbnail_360x195(origin_path, dest_path, quality=70):
    """Resize image to 360x195.
    As horizontal direction precedes, vertical direction is possible to get white spaces."""

    pil_origin = Image.open(origin_path)
    w, h = pil_origin.size

    # 横幅360px。
    resize_rate = 360/w
    pil_w360 = pil_origin.resize((int(w*resize_rate), int(h*resize_rate)))
    w, h = pil_w360.size

    # 360x195。
    bg = Image.new('RGB', [360, 195], (255, 255, 255))
    bg.paste(pil_w360, (0, int((195-h)/2)))

    bg.save(dest_path, quality=quality)
