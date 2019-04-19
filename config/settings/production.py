from .base import *

DEBUG = False

# TODO: Must be False on the real production environment.
# This status maybe set in DB.
SHOW_500_ERROR = True

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
