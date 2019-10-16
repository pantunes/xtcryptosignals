__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os


BINANCE_API_KEY = ''  # Add Personal Binance API KEY
BINANCE_API_SECRET = ''  # Add Personal Binance API SECRET

CORS_ALLOWED_ORIGINS = (
    'http://127.0.0.1:8000',
    'https://xtcryptosignals.com',
)

try:
    GA_TRACKING_ID = os.environ['GA_TRACKING_ID']
except KeyError:
    GA_TRACKING_ID = None
