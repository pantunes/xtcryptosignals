__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime
from flask import (
    Blueprint,
    current_app,
    render_template,
    url_for,
    g,
)
from xtcryptosignals.client import service
from xtcryptosignals import __version__
from xtcryptosignals.common.utils import (
    get_pairs,
    get_coin_tokens,
)
from xtcryptosignals.client.utils import validate_args


bp = Blueprint("tools", __name__)


@bp.before_request
def before_request():
    g.SYMBOLS_PER_EXCHANGE, _ = service.get_symbols_per_exchange()
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()
    g.COINS_OR_TOKENS_REFERENCE, _ = service.get_coins_or_tokens_reference()


@bp.context_processor
def context_processor():
    return dict(
        version=__version__,
        ga_tracking_id=current_app.config["GA_TRACKING_ID"],
        current_year=datetime.utcnow().year,
        frequencies=g.HISTORY_FREQUENCY,
        pairs=get_pairs(g.SYMBOLS_PER_EXCHANGE),
        tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE, show_all=True),
    )


@bp.route("/tools/fear-and-greed")
def fear_and_greed():
    _min = g.HISTORY_FREQUENCY.index(current_app.config["CFGI_MIN"])
    _max = g.HISTORY_FREQUENCY.index(current_app.config["CFGI_MAX"])

    chart_frequencies = g.HISTORY_FREQUENCY[_min:_max]

    return render_template(
        template_name_or_list="tools/fear-and-greed.html",
        frequency=current_app.config["CFGI_MIN"],
        chart_frequencies=chart_frequencies,
        quote="USDT",
    )


@bp.route("/tools/coin-or-token/<coin_or_token>")
def coin_or_token_frequency(coin_or_token):
    return render_template(
        template_name_or_list="tools/coin-token.html",
        socket_base_url=current_app.config["SOCKET_BASE_URL"],
        frequency=g.HISTORY_FREQUENCY[0],
        frequencies_charts=["10s", "10m", "30m", "1h", "4h", "12h", "1d", "4w"],
        attributes={"price_usdt": "Price USDT"},
        coin_or_token=coin_or_token,
        reference=g.COINS_OR_TOKENS_REFERENCE[coin_or_token],
    )


@bp.route("/tools/tether/<coin_or_token>")
@validate_args()
def tether(coin_or_token):
    if coin_or_token != "BTC":
        raise ValueError("Coin/Token not supported for now.")

    return dict(
        template_name_or_list="tools/tether.html",
        frequency=g.HISTORY_FREQUENCY[0],
        frequencies_charts=["1h", "1d", "1w", "4w"],
        coin_or_token=coin_or_token,
        reference=g.COINS_OR_TOKENS_REFERENCE[coin_or_token],
    )


@bp.route("/tools/twitter/<frequency>")
@validate_args()
def twitter(frequency):
    if frequency != "1d":
        raise ValueError("Frequency not supported for now.")

    projects, status = service.get_projects()
    if status != 200:
        raise ValueError("Could not fetch Projects.")

    projects_twitter = []
    for p in projects:
        project_last_tweet, _ = service.get_project_last_tweet(p["_id"])
        if project_last_tweet.get("num_followers") is None:
            continue
        projects_twitter.append(p["_id"])

    return dict(
        template_name_or_list="tools/twitter.html",
        frequency=g.HISTORY_FREQUENCY[0],
        twitter_frequency="1d",
        projects_twitter=projects_twitter,
    )


@bp.route("/spotlight/search")
def spotlight_search():
    rows = []

    for coin_or_token in g.COINS_OR_TOKENS_REFERENCE:
        url = url_for(
            "ticker.token_frequency",
            coin_or_token=coin_or_token,
            frequency=g.HISTORY_FREQUENCY[0],
        )
        rows.append(dict(label=coin_or_token, value=coin_or_token, url=url))

    for pair in get_pairs(g.SYMBOLS_PER_EXCHANGE):
        url = url_for(
            "ticker.pair_frequency", pair=pair, frequency=g.HISTORY_FREQUENCY[0]
        )
        rows.append(dict(label=pair, value=pair, url=url))

    url = url_for("tools.fear_and_greed")
    rows.append(dict(label="Fear and Greed", value="Fear and Greed", url=url))

    url = url_for("tools.twitter", frequency="1d")
    rows.append(dict(label="Twitter", value="Twitter", url=url))

    url = url_for("tools.tether", coin_or_token="BTC")
    rows.append(dict(label="Tether", value="Tether", url=url))

    # Auth
    url = url_for("ticker.favourites", frequency="1d")
    rows.append(dict(label="Favourites", value="Favourites", url=url))

    url = url_for("transaction.index")
    rows.append(dict(label="Transactions", value="Transactions", url=url))

    url = url_for("portfolio.index")
    rows.append(dict(label="Portfolio", value="Portfolio", url=url))

    url = url_for("notification.index")
    rows.append(dict(label="Notifications", value="Notifications", url=url))

    url = url_for("exchange.index", exchange="binance")
    rows.append(dict(label="Binance", value="Binance", url=url))

    return dict(count=len(rows), rows=rows)
