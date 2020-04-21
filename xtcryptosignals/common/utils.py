__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
import wikipediaapi
from millify import millify
from bs4 import BeautifulSoup
from functools import wraps
from mongoengine import connect


def use_mongodb(**config_params):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            connect(**config_params)
            return f(*args, **kwargs)

        return wrapper

    return decorator


def get_pairs(symbols_per_exchange):
    pairs = set()
    for i in symbols_per_exchange:
        for _, b in i.items():
            for c, d in b["pairs"]:
                pairs.add(c + d)
    return ["ALL"] + sorted(pairs)


def get_coin_tokens(symbols_per_exchange):
    tokens = set()
    for i in symbols_per_exchange:
        for _, b in i.items():
            for c, _ in b["pairs"]:
                tokens.add(c)
    return sorted(tokens)


def get_wikipedia_summary(url):
    if url is None:
        return
    wiki_wiki = wikipediaapi.Wikipedia("en")
    page_py = wiki_wiki.page(url.rsplit("/", 1)[-1])
    p = page_py.summary[0:1000]
    return p[: p.rfind(". ") + 1]


def get_twitter_num_followers(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    try:
        return millify(
            soup.find(href=f"/{url.rsplit('/', 1)[-1]}/followers").find(
                attrs={"class": "ProfileNav-value"}
            )["data-count"],
            precision=2,
        )
    except AttributeError:
        return "?"
