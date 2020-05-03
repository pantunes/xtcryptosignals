__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
import requests
from datetime import datetime
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.tasks.models.cfgi import CFGI
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)


@task(bind=True)
@use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
def update(self):
    logger = self.get_logger()

    try:
        response = requests.get(url=s.URL_CFGI)
        x = response.json()["data"][0]
        index = x["value"]
        added_on = datetime.fromtimestamp(int(x["timestamp"])).date()
        kwargs = dict(index=index, added_on=added_on)
        CFGI(**kwargs).save()
        red.set(s.REDIS_CFGI, index)
    except Exception as error:
        logger.error("cfgi error: {}".format(str(error)))
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
