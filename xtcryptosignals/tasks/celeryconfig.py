__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from celery.schedules import crontab
from xtcryptosignals.tasks import settings as s


CELERY_DEFAULT_QUEUE = "XTCryptoSignals"

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]

CELERY_IGNORE_RESULT = True
CELERY_TIMEZONE = "UTC"

BROKER_URL = s.BROKER_URL

CELERY_IMPORTS = (
    "xtcryptosignals.tasks.ticker",
    "xtcryptosignals.tasks.notifications",
    "xtcryptosignals.tasks.cfgi",
)

CELERYBEAT_SCHEDULE = {
    "ticker": {
        "task": "xtcryptosignals.tasks.ticker.update",
        "schedule": s.TICKER_SCHEDULE,
    },
    "notifications": {
        "task": "xtcryptosignals.tasks.notifications.update",
        "schedule": s.TICKER_SCHEDULE,
    },
    "cfgi": {
        "task": "xtcryptosignals.tasks.cfgi.update",
        "schedule": crontab(hour=5, minute=30),
    },
}
