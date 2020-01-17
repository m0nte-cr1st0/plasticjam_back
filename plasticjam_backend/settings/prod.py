from .base import *

CORS_ORIGIN_ALLOW_ALL = True

GENERATE_AUTO_DOCS = True

LOGGING_FOLDER = config('GCL_LOGGING_FOLDER', default=os.path.abspath(os.path.join(BASE_DIR, '..', 'logs')))
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
            'filename': os.path.join(LOGGING_FOLDER, 'gcl_django_errors.log'),
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
