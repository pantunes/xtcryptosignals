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

CELERY_ALWAYS_EAGER = CELERY_EAGER_PROPAGATES_EXCEPTIONS = False

CELERY_IGNORE_RESULT = True
CELERY_TIMEZONE = "UTC"

# Number of child processes created by main worker process, defaults to the
# number of CPUs available in the machine
# CELERYD_CONCURRENCY = 2

BROKER_URL = s.BROKER_URL

CELERY_IMPORTS = (
    "xtcryptosignals.tasks.ticker",
    "xtcryptosignals.tasks.notifications",
    "xtcryptosignals.tasks.cfgi",
    "xtcryptosignals.tasks.project",
    "xtcryptosignals.tasks.tether",
    "xtcryptosignals.tasks.order_book",
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
    "project": {
        "task": "xtcryptosignals.tasks.project.update",
        "schedule": crontab(hour=23, minute=59),
    },
    "tether": {
        "task": "xtcryptosignals.tasks.tether.update",
        "schedule": crontab(hour="*", minute=1),
    },
    "order_book": {
        "task": "xtcryptosignals.tasks.order_book.update",
        "schedule": s.ORDER_BOOK_SCHEDULE,
    },
}
