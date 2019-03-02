__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.models.history import History
import xtcryptosignals.settings as s


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
