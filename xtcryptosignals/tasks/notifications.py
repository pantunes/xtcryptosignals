__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
import json
import redis
import hashlib
import telegram
from datetime import timedelta
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from pywebpush import webpush, WebPushException
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.tasks.utils import convert_to_seconds
from xtcryptosignals.server.api.notifications.models import (
    NotificationRule,
    Notification,
)
from xtcryptosignals.tasks.models.history import History
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)

PATH_LOGOS = f"{os.path.dirname(os.path.realpath(__file__))}/../client/static/imgs/logos/"


@task(bind=True)
@use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
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
                '<a href="{domain}/ticker/source/{ticker}/10s">{ticker}'
                "</a> {metric} is {direction} {change}% within "
                "{interval}. Current Price is {price:,.4f} USDT."
            )
        else:
            message_templ = (
                '<a href="{domain}/ticker/source/{ticker}/10s">{ticker}'
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

        message_web = message_templ.format(
            domain=s.WEBSITE_ADDRESS,
            ticker=obj_history["ticker"],
            metric=notif.metric.capitalize(),
            direction=direction,
            change=obj_history_change,
            interval=notif.interval,
            price=price,
        )

        key = "{}{}".format(notif.user.pk, message_web)
        hash_object = hashlib.md5(key.encode())
        redis_key = hash_object.hexdigest()

        if red.get(redis_key):
            logger.warning(
                "Already sent notifications to {}".format(notif.user.pk)
            )
            continue

        red.setex(
            name=redis_key,
            value=1,
            time=timedelta(seconds=convert_to_seconds(notif.interval)),
        )

        notification_kwargs = dict(
            coin_token=obj_history["ticker"],
            message=message_web,
            user=notif.user,
        )
        if notif.metric == "price":
            notification_kwargs.update(is_positive=(direction is "up"))

        Notification(**notification_kwargs).save()

        message_push_notification = message_web.replace(
            '<a href="{domain}/ticker/source/{ticker}/10s">{ticker}</a>'.format(
                domain=s.WEBSITE_ADDRESS, ticker=obj_history["ticker"]
            ),
            obj_history["ticker"],
        )

        try:
            try:
                logger.warning(
                    "Sending web notification to {}".format(notif.user.pk)
                )
                webpush(
                    subscription_info=notif.user.metadata["subscription"],
                    data=json.dumps(
                        dict(
                            title="XTCryptoSignals",
                            message=message_push_notification,
                            url="{}/ticker/{symbol}/{frequency}".format(
                                s.WEBSITE_ADDRESS, **obj_history
                            ),
                            icon="{}{ticker}.png".format(
                                s.STATIC_COINS_TOKENS_LOGOS_FOLDER,
                                **obj_history,
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
            logger.error("web notification error: {}".format(str(error)))
            self.update_state(state=states.FAILURE, meta=str(error))
            raise Ignore()

        heart = "💚" if direction is "up" else "❤️"
        try:
            logger.warning("Sending telegram notification")
            bot = telegram.Bot(token=s.TELEGRAM_BOT_TOKEN)
            with open(
                f"{PATH_LOGOS}{obj_history['ticker']}@128.png", "rb",
            ) as photo:
                bot.send_photo(
                    chat_id=s.TELEGRAM_GROUP_CHAT_ID,
                    photo=photo,
                    caption=f"{heart} {message_web}",
                    parse_mode=telegram.ParseMode.HTML,
                )
        except Exception as error:
            logger.error("telegram notification error: {}".format(str(error)))
            self.update_state(state=states.FAILURE, meta=str(error))
            raise Ignore()
