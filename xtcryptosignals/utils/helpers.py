__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from importlib import import_module
from xtcryptosignals.models.history import History
import xtcryptosignals.settings as s


def get_class(folder, module):
    exchange_module = import_module(
        '{}.{}'.format(folder, module)
    )
    return getattr(exchange_module, module.capitalize())


def convert_to_seconds(x):
    _t = x[-1]
    seconds = int(x[:-1])
    if _t == 's':
        return seconds
    minutes = seconds * 60
    if _t == 'm':
        return minutes
    hours = minutes * 60 * 60
    if _t == 'h':
        return hours
    days = hours * 24
    if _t == 'd':
        return days
    weeks = days * 7
    if _t == 'w':
        return weeks
    raise ValueError('Undefined item: {}'.format(x))


def get_ticker_data_from_namespace(namespace):
    model = type('History{}'.format(namespace[1:]), (History,), {})
    rows = []
    for x in s.SYMBOLS_PER_EXCHANGE:
        for exchange, items in x.items():
            for symbol in [x[0]+x[1] for x in items['pairs']]:
                row = model.objects(
                    symbol=symbol,
                    source=exchange
                ).first()
                if not row:
                    continue
                rows.append(row.get_object(frequency=namespace[1:]))
    return rows
