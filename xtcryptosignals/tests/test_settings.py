__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals import settings as s
from xtcryptosignals.utils.helpers import convert_to_seconds


def test_ticker_schedule():
    assert s.TICKER_SCHEDULE <= convert_to_seconds(s.HISTORY_FREQUENCY[0])


def test_settings():
    assert s.DEBUG
    assert s.MONGODB_NAME
    assert s.TICKER_SCHEDULE
    assert s.TIMEOUT_PER_SYMBOL_REQUEST
    assert s.TIMEOUT_PER_SYMBOLS_REQUEST
    assert s.SYMBOL_FLOAT_PRECISION
