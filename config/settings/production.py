import pymysql
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': env.db(),
}

pymysql.install_as_MySQLdb()

STATIC_ROOT = '/var/www/static'

MEDIA_ROOT = '/var/www/media'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/mrrhp-apache/error.log',
            'formatter': 'production',
            'when': 'D',  # Day
            'interval': 1,  # Day by day
            'backupCount': 7,  # Log generation
        },
        'django-axes': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/mrrhp-apache/django-axes.log',
            'formatter': 'production',
            'when': 'D',  # Day
            'interval': 1,  # Day by day
            'backupCount': 7,  # Log generation
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django-axes-logger': {
            'handlers': ['django-axes'],
            # level を INFO にすると以下のようなログがアクセスのたびに吐かれる。
            #   BEGIN LOG
            #   Using django-axes version 5.2.0
            #   blocking by IP only.
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
