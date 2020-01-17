from .base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True

CORS_BLOCKED_URLS = ['user-detail']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')
