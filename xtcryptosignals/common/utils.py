__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from functools import wraps
from mongoengine import connect, disconnect


def use_mongodb(**config_params):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            connect(**config_params)
            f(*args, **kwargs)
            disconnect()

        return wrapper

    return decorator


def get_pairs(symbols_per_exchange, show_all=True):
    pairs = set()
    for i in symbols_per_exchange:
        for _, b in i.items():
            for c, d in b["pairs"]:
                pairs.add(c + d)

    if show_all:
        return ["ALL"] + sorted(pairs)

    return sorted(pairs)


def get_pairs_ex(symbols_per_exchange):
    pairs = dict()
    for i in symbols_per_exchange:
        for _, b in i.items():
            for c, d in b["pairs"]:
                pairs[c + d] = dict(token=c, pair=d)
    return pairs


def get_coin_tokens(symbols_per_exchange, show_all=False):
    tokens = set()
    for i in symbols_per_exchange:
        for _, b in i.items():
            for c, _ in b["pairs"]:
                tokens.add(c)

    if show_all:
        return ["ALL"] + sorted(tokens)

    return sorted(tokens)
