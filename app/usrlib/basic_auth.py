
"""Basic Auth lib

ref: https://qiita.com/yukilab/items/b0467b6988657bc8950d

# How to use
if not basic_auth.basic_auth(request):
    return basic_auth.http401()

ID,PW are made with createsuperuser.
"""

import base64
from django.contrib.auth import authenticate
from django.http import HttpResponse


def http401():
    response = HttpResponse("Unauthorized", status=401)
    response['WWW-Authenticate'] = 'Basic realm="basic auth username/password inalid"'
    return response


def basic_auth(request):
    """
    :param request:
    :return: True is authenticated. Otherwise return False
    """
    if 'HTTP_AUTHORIZATION' not in request.META:
        return False
    (auth_scheme, base64_username_pass) = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
    if auth_scheme.lower() != 'basic':
        return http401()
    username_pass = base64.decodebytes(base64_username_pass.strip().encode('ascii')).decode('ascii')
    (username, password) = username_pass.split(':', 1)
    user = authenticate(username=username, password=password)
    return user is not None
