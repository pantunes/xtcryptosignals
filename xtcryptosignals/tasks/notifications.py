__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

import json
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from pywebpush import webpush, WebPushException
from xtcryptosignals.tasks import settings as s
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.server.api.user.models import User


@task(bind=True)
@use_mongodb(
    db=s.MONGODB_NAME,
    host=s.MONGODB_HOST,
    port=s.MONGODB_PORT,
    connect=False
)
def update(self):
    logger = self.get_logger()
    logger.warning('Notifications')

    user = User.objects().first()
    subscription_information = user.metadata['subscription']

    try:
        try:
            webpush(
                subscription_info=subscription_information,
                data=json.dumps(dict(
                    title='XTCryptoSignals',
                    message='BTC is up 7%',
                    url='http://127.0.0.1:8000/ticker/BTCUSDT/10s',
                    icon='/static/imgs/logos/BTC.png',
                )),
                vapid_private_key=s.VAPID_PRIVATE_KEY,
                vapid_claims=dict(sub='mailto:{}'.format(s.VAPID_CLAIMS)),
            )
        except WebPushException as error:
            if error.response and error.response.json():
                extra = error.response.json()
                logger.error(
                    "Remote service replied with a {}:{}, {}",
                    extra.code,
                    extra.errno,
                    extra.message
                )
    except ValueError as error:
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
    finally:
        pass
