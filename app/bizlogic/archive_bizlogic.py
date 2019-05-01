
"""Draft bizlogic
"""

import os
from django.conf import settings
from app.usrlib import image_utils, common
import shutil
from app.models import *
import datetime
import re
from app.bizlogic import image_bizlogic
from django.utils import timezone


def register_all_archive_posts() -> None:
    """Extract data from __drafts, archives folder and register them into DB."""

    # Get all existing post folder paths. Sorted from past to now.
    DRAFT_TOP_DIR = os.path.join(settings.BASE_DIR, '__drafts')
    draft_dirs = filter(os.path.isdir,
                        map(lambda _: os.path.join(DRAFT_TOP_DIR, _),
                            sorted(os.listdir(DRAFT_TOP_DIR))))

    # UPSERT MODE -----------------------------------------
    for dirpath in draft_dirs:
        archive_post = __create_archive_post_obj(dirpath)
        Post.objects.update_or_create(
            code=archive_post.code,
            defaults={
                'publish_at': archive_post.publish_at,
                'title_ja': archive_post.title_ja,
                'title_en': archive_post.title_en,
                'tag': archive_post.tag,
                'year': archive_post.year,
                'thumbnail': archive_post.thumbnail,
                'body_ja': archive_post.body_ja,
                'body_en': archive_post.body_en,
                'html': archive_post.html,
            },
        )

    # BULK_INSERT MODE -----------------------------------------
    # Create Post object one by one.
    # Cuz images will be copied within method, they will exist before registering Post.
    # Obstructs image duplication as well.
    # post_objs = (__create_archive_post_obj(dirpath) for dirpath in draft_dirs)
    # Post.objects.bulk_create(post_objs)


def __create_archive_post_obj(dirpath) -> Post:
    """Extract archive data and create Post object with it."""

    # Create new image names. {0.jpg : uniquename}
    MARKDOWNX_DIR = os.path.join(settings.MEDIA_ROOT, 'markdownx')
    image_correspondence_table = {
        basename: image_utils.get_unique_image_name(basename, MARKDOWNX_DIR)
        for basename in image_utils.get_image_basenames(dirpath)
    }

    # Copy images to media folder with new unique names. 0.jpg -> /media/markdownx/uniquename
    for origin, new_basename in image_correspondence_table.items():
        shutil.copyfile(os.path.join(dirpath, origin),
                        os.path.join(MARKDOWNX_DIR, new_basename))

    # Get data of archive file.
    archive_data = __extract_archive_data(dirpath)

    # Create thumbnail for this post.
    thumbnail_basename = (image_correspondence_table[archive_data['mainimage']]
                          if archive_data['mainimage'] in image_correspondence_table
                          else None)
    if thumbnail_basename:
        image_bizlogic.generate_thumbnail(thumbnail_basename)

    # Create Post object.
    return Post(
        # Here set time with Japan timezone, then it will be registered with UTC in DB, minus 9 hours.
        publish_at=datetime.datetime.strptime(archive_data['publishdate']+'+0900', '%Y-%m-%d%z') ,
        code      =archive_data['code']                                                          ,
        title_ja  =archive_data['title_ja']                                                      ,
        title_en  =archive_data['title_en']                                                      ,
        tag       =Tag.objects.filter(name_ja=archive_data['tag']).first()                       ,
        year      =Year.objects.filter(code=archive_data['publishdate'][:4]).first()             ,
        thumbnail =thumbnail_basename                                                            ,
        body_ja   =__manipulate_body_content(archive_data['ja_md']  , image_correspondence_table),
        body_en   =__manipulate_body_content(archive_data['en_md']  , image_correspondence_table),
        html      =__manipulate_body_content(archive_data['ja_html'], image_correspondence_table),
    )


def __extract_archive_data(dirpath) -> dict:
    """Extract data required only from archive files."""

    # Each path.
    JA_MD = os.path.join(dirpath, 'ja.md')
    EN_MD = os.path.join(dirpath, 'en.md')
    JA_HTML = os.path.join(dirpath, 'ja.html')

    # Get markdown meta data.
    meta = common.get_markdown_metadata(JA_MD)

    # Extract data.
    # There are little difference between having html(older posts) and not having html(newer posts).
    has_html = os.path.isfile(JA_HTML)
    return {
        'publishdate': meta['publishdate'][0],
        'code'       : meta['code'       ][0],
        'title_ja'   : meta['title_ja'   ][0],
        'title_en'   : meta['title_en'   ][0],
        'tag'        : meta['tag'        ][0],
        'mainimage'  : meta['mainimage'  ][0],
        'ja_md'      : '' if has_html else common.read_file(JA_MD)  ,
        'en_md'      : '' if has_html else common.read_file(EN_MD)  ,
        'ja_html'    : common.read_file(JA_HTML) if has_html else '',
    }


def __manipulate_body_content(string, image_correspondence_table):
    """Manipulate body."""

    # Replace image paths.
    for key, value in image_correspondence_table.items():
        string = (string
                    .replace(f'![]({key})', f'![](/media/markdownx/{value})')
                    .replace(f'src="{key}"', f'src="/media/markdownx/{value}"')
        )

    # Remove meta description in markdown file. Looks very bizlogic.
    for r in [
        r'publishdate: .*?\n' ,
        r'publish: .*?\n'     ,
        r'code: .*?\n'        ,
        r'title_ja: .*?\n'    ,
        r'title_en: .*?\n'    ,
        r'tag: .*?\n'         ,
        r'author: .*?\n'      ,
        r'hash: .*?\n'        ,
        r'originaleid: .*?\n' ,
        r'mainimage: .*?\n'   ,
        r'convert2html: .*?\n',
    ]:
        string = re.sub(r, '', string)
    return string
