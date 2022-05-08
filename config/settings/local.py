import os
from .base import *  # noqa: F403

DEBUG = True

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # noqa: F405
