__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os


IP_ADDRESS = '0.0.0.0'
PORT_SERVER = 5000
PORT_CLIENT = 8000

try:
    SERVER_API_BASE_URL = os.environ['SERVER_API_BASE_URL']
except KeyError:
    # development
    SERVER_API_BASE_URL = 'http://127.0.0.1:{}/'.format(PORT_SERVER)


BINANCE_API_KEY = ''  # Add Personal Binance API KEY
BINANCE_API_SECRET = ''  # Add Personal Binance API SECRET
