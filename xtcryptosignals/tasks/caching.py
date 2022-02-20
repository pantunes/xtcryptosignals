__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
import json
import requests
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.tasks.models.history import History
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)


@use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
def prepare_cache():
    # cache crypto & fear index
    response = requests.get(url=s.URL_CFGI)
    cfgi = response.json()["data"][0]["value"]
    red.set(s.REDIS_CFGI, cfgi)
    print(f"Caching CFGI: {cfgi}")

    # cache last price per History Model
    for f in s.HISTORY_FREQUENCY:
        for x in s.SYMBOLS_PER_EXCHANGE:
            for exchange, items in x.items():
                for symbol in [x[0] + x[1] for x in items["pairs"]]:
                    model_history = type(f"History{f}", (History,), {})
                    row = model_history.objects(
                        symbol=symbol, source=exchange
                    ).first()
                    if not row:
                        print(f"No need to Cache, db is empty")
                        continue
                    row = row.to_dict(frequency=f)
                    key = s.REDIS_KEY_TICKER.format(**row)
                    ser_row = json.dumps(row)
                    red.set(key, ser_row)
                    print(f"Caching {key}: {row['price']}")
