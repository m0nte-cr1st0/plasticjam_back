from .base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['plastickjambackend.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True

CORS_BLOCKED_URLS = ['user-detail']

GENERATE_AUTO_DOCS = True

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')

LOGGING_FOLDER = os.path.abspath(os.path.join(BASE_DIR, '..', 'logs'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(name)s] %(levelname)s %(asctime)s\n%(message)s'
        },
    },
    'handlers': {
        # Send all messages to console
        'filelog': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_FOLDER, 'plasticjam_django_errors.log'),
            'when': 'D',
            'interval': 7,
            'backupCount': 4,
        },
    },
    'loggers': {
        # This is the "catch all" logger
        'django': {
            'handlers': ['filelog'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
