# Only for demo project. It's a bad practice upload this file to repository
from .base import *


ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plasticjam_db',
        'USER': 'plasticjam_user',
        'PASSWORD': 'plasticjam_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_BLOCKED_URLS = ['users-detail']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')
