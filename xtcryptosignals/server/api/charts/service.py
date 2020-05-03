__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime
from xtcryptosignals.tasks.models.history import History
from xtcryptosignals.tasks.models.cfgi import CFGI
from xtcryptosignals.tasks.models.tether import Tether
from xtcryptosignals.tasks.models.project_twitter import ProjectTwitter
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.tasks import settings as s


NUM_OCCURRENCES = 30  # CFGI_MIN=1d in client


def _get_exchange_pair_reference(coin_or_token):
    try:
        return s.EXCHANGES_AND_PAIRS_OF_REFERENCE[coin_or_token]
    except KeyError:
        raise ValueError("Coin/Token is incorrect.")


def get_chart_fear_and_greed_index(frequency, coin_or_token):
    try:
        ref = _get_exchange_pair_reference(coin_or_token)
    except ValueError as err:
        return dict(error=str(err)), 400

    model_history = type("History{}".format(frequency), (History,), {})
    rows = model_history.objects(
        symbol=coin_or_token + ref["pair"], source=ref["name"],
    )[:NUM_OCCURRENCES]

    btc_prices = {
        x.created_on.strftime("%Y-%m-%d"): int(x.price_usdt) for x in rows
    }

    cfgi_values = {
        x.added_on.strftime("%Y-%m-%d"): x.index
        for x in CFGI.objects[
            : (NUM_OCCURRENCES * 12)
        ]  # CFGI_MAX=12w in client
    }

    days = list(btc_prices.keys())
    days.reverse()

    cfgi = []
    for x in days:
        try:
            cfgi.append(cfgi_values[x])
        except KeyError:
            cfgi.append(None)

    return dict(days=days, BTC=[btc_prices[x] for x in days], cfgi=cfgi,)


def get_chart_coin_or_token_frequency(coin_or_token, frequency):
    try:
        ref = _get_exchange_pair_reference(coin_or_token)
    except ValueError as err:
        return dict(error=str(err)), 400

    model_history = type("History{}".format(frequency), (History,), {})
    rows = model_history.objects(
        symbol=coin_or_token + ref["pair"], source=ref["name"],
    )[:100]

    prices = []
    volumes = []
    num_trades = []

    for row in rows:
        obj = row.to_dict(frequency=frequency)
        prices.append([obj["created_on_ts"], obj["price_usdt"]])
        volumes.append([obj["created_on_ts"], obj["volume_24h"]])
        num_trades.append([obj["created_on_ts"], obj.get("number_trades_24h")])

    prices.reverse()
    volumes.reverse()
    num_trades.reverse()

    return dict(prices=prices, volumes=volumes, num_trades=num_trades,)


def _normalize_ts(ts, frequency):
    if frequency == "1h":
        kwargs = dict(minute=0, second=0, microsecond=0)
    else:
        kwargs = dict(hour=0, minute=0, second=0, microsecond=0)
    return (
        datetime.timestamp(datetime.fromtimestamp(ts / 1000).replace(**kwargs))
        * 1000
    )


def get_chart_tether_btc(coin_or_token, frequency):
    try:
        ref = _get_exchange_pair_reference(coin_or_token)
    except ValueError as err:
        return dict(error=str(err)), 400

    model_history = type("History{}".format(frequency), (History,), {})
    rows = model_history.objects(
        symbol=coin_or_token + ref["pair"], source=ref["name"],
    )[:NUM_OCCURRENCES]

    btc_prices = {}
    for row in rows:
        obj = row.to_dict(frequency=frequency)
        btc_prices[_normalize_ts(obj["created_on_ts"], frequency)] = obj[
            "price_usdt"
        ]

    tether = {}
    for row in Tether.objects[: (NUM_OCCURRENCES * 8 * 12)]:
        obj = row.to_dict()
        ts = _normalize_ts(obj["created_on_ts"], frequency)
        tether[ts] = (
            obj["total_supply_eth"],
            obj["num_holders_eth"],
        )

    days = list(btc_prices.keys())
    days.reverse()

    tether_max_supply_erc20 = []
    tether_num_hodlers_erc20 = []
    for x in days:
        try:
            tether_max_supply_erc20.append([x, tether[x][0]])
        except KeyError:
            pass
        try:
            tether_num_hodlers_erc20.append([x, tether[x][1]])
        except KeyError:
            pass

    return dict(
        tether_max_supply_erc20=tether_max_supply_erc20,
        tether_num_hodlers_erc20=tether_num_hodlers_erc20,
        prices=[[x, btc_prices[x]] for x in days],
    )


def get_chart_twitter():
    projects_twitter = {}

    for p in Project.objects:
        project_name = f"{p.name.replace(' ', '_')}_{p.coin_or_token}"
        projects_twitter[project_name] = []
        for t in ProjectTwitter.objects(project=p)[:30]:
            if not t:
                continue
            obj = t.to_dict()
            try:
                projects_twitter[project_name].append(
                    [
                        _normalize_ts(obj["created_on_ts"], "1d"),
                        obj["num_followers"],
                    ]
                )
            except KeyError:
                pass
        if not any(projects_twitter[project_name]):
            del projects_twitter[project_name]
        else:
            projects_twitter[project_name].reverse()

    return dict(projects_twitter=projects_twitter)
