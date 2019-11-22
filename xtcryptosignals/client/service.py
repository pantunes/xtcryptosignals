__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import current_app


def get_history_frequency():
    response = requests.get(
        url='{}tokens/frequency'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
    )
    return response.json(), response.status_code


def get_symbols_per_exchange():
    response = requests.get(
        url='{}tokens/symbols'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
    )
    return response.json(), response.status_code
