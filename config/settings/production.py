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
