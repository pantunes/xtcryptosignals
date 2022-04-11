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

from xtcryptosignals.tasks import settings as s

red = redis.Redis.from_url(s.BROKER_URL)


def get_ticker_pair_last(pair):
    key = s.REDIS_KEY_TICKER.format(
        source=s.BINANCE,
        symbol=pair,
        frequency=s.HISTORY_FREQUENCY[0],
    )

    ser_row = red.get(key)
    if not ser_row:
        return

    return json.loads(ser_row)
