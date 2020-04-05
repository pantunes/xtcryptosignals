__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import json
import redis
import hashlib
from datetime import timedelta
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from pywebpush import webpush, WebPushException
from xtcryptosignals.tasks import settings as s
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.tasks.utils import convert_to_seconds
from xtcryptosignals.server.api.notifications.models import (
    NotificationRule,
    Notification,
)
from xtcryptosignals.tasks.models.history import History


red = redis.Redis.from_url(s.BROKER_URL)


@task(bind=True)
@use_mongodb(
    db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT,
)
def update(self):
    logger = self.get_logger()

    for notif in NotificationRule.objects():
        exchange_and_pair = s.EXCHANGES_AND_PAIRS_OF_REFERENCE[notif.coin_token]

        model_history = type("History{}".format(notif.interval), (History,), {})
        row_history = model_history.objects(
            symbol=notif.coin_token + exchange_and_pair["pair"],
            source=exchange_and_pair["name"],
        ).first()

        if not row_history:
            continue

        obj_history = row_history.to_dict(frequency=notif.interval)

        try:
            obj_history_change = obj_history["{}_change".format(notif.metric)]
        except KeyError:
            continue

        try:
            price = obj_history["price_usdt"]
        except KeyError:
            continue

        if price < 1:
            message_templ = (
                '<a href="/ticker/source/{ticker}/10s">{ticker}'
                "</a> {metric} is {direction} {change}% within "
                "{interval}. Current Price is {price:,.4f} USDT."
            )
        else:
            message_templ = (
                '<a href="/ticker/source/{ticker}/10s">{ticker}'
                "</a> {metric} is {direction} {change}% within "
                "{interval}. Current Price is {price:,.2f} USDT."
            )

        if notif.percentage > 0.0:
            if obj_history_change < notif.percentage:
                continue

            direction = "up"

        elif obj_history_change > notif.percentage:
            continue

        else:
            direction = "down"

        logger.warning(
            "{} {}_change {} {}% {}".format(
                obj_history["ticker"],
                notif.metric,
                direction,
                obj_history_change,
                notif.interval,
            )
        )

        message = message_templ.format(
            ticker=obj_history["ticker"],
            metric=notif.metric.capitalize(),
            direction=direction,
            change=obj_history_change,
            interval=notif.interval,
            price=price,
        )

        key = "{}{}".format(notif.user.pk, message)
        hash_object = hashlib.md5(key.encode())
        redis_key = hash_object.hexdigest()

        if red.get(redis_key):
            logger.warning("Already sent notif. to {}".format(notif.user.pk))
            continue

        red.setex(
            name=redis_key,
            value=1,
            time=timedelta(seconds=convert_to_seconds(notif.interval)),
        )

        notif_kwargs = dict(
            coin_token=obj_history["ticker"], message=message, user=notif.user,
        )
        if notif.metric == "price":
            notif_kwargs.update(is_positive=(direction is "up"))

        Notification(**notif_kwargs).save()

        message = message.replace(
            '<a href="/ticker/source/{ticker}/10s">{ticker}</a>'.format(
                ticker=obj_history["ticker"]
            ),
            obj_history["ticker"],
        )

        try:
            try:
                logger.warning("Sending notif. to {}".format(notif.user.pk))
                webpush(
                    subscription_info=notif.user.metadata["subscription"],
                    data=json.dumps(
                        dict(
                            title="XTCryptoSignals",
                            message=message,
                            url="{}/ticker/{symbol}/{frequency}".format(
                                s.SERVER_ADDRESS, **obj_history
                            ),
                            icon="{}{ticker}.png".format(
                                s.STATIC_COINS_TOKENS_LOGOS_FOLDER,
                                **obj_history
                            ),
                        )
                    ),
                    vapid_private_key=s.VAPID_PRIVATE_KEY,
                    vapid_claims=dict(sub="mailto:{}".format(s.VAPID_CLAIMS)),
                )
            except WebPushException as error:
                if error.response and error.response.json():
                    extra = error.response.json()
                    logger.error(
                        "Remote service replied with a {}:{}, {}",
                        extra.code,
                        extra.errno,
                        extra.message,
                    )
        except Exception as error:
            logger.error("notifications error: {}".format(str(error)))
            self.update_state(state=states.FAILURE, meta=str(error))
            raise Ignore()
        finally:
            pass
