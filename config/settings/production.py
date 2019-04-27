import pymysql
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'app'                     ,
        'USER'     : 'root'                    ,
        'PASSWORD' : 'password'                ,
        'HOST'     : 'localhost'               ,
        'PORT'     : '3306'                    ,  # 3306 is default
        # ssl 通信のために必要らしいけどまだ不明。
        # 'OPTIONS': {'ssl': {'ca' : 'ca_path',
        #                     'key' : 'key_path',
        #                     'cert' : 'cert_path'}},
    }
}

pymysql.install_as_MySQLdb()

STATIC_ROOT = '/var/www/static'

MEDIA_ROOT = '/var/www/media'
