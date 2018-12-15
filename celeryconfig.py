__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import xtcryptosignals.settings as s


CELERY_DEFAULT_QUEUE = 'xtcrypto-signals'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

CELERY_IGNORE_RESULT = True
CELERY_TIMEZONE = 'UTC'

BROKER_URL = 'redis://localhost:6379'

CELERY_IMPORTS = (
    'xtcryptosignals.tasks.ticker',
)

CELERYBEAT_SCHEDULE = {
    'ticker': {
        'task': 'xtcryptosignals.tasks.ticker.update',
        'schedule': s.TICKER_SCHEDULE
    }
}
