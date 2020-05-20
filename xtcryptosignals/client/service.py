__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import current_app


def get_history_frequency():
    response = requests.get(
        url="{}tokens/frequency".format(
            current_app.config["SERVER_API_BASE_URL"]
        ),
    )
    return response.json(), response.status_code


def get_symbols_per_exchange():
    response = requests.get(
        url="{}tokens/symbols".format(
            current_app.config["SERVER_API_BASE_URL"]
        ),
    )
    return response.json(), response.status_code


def get_coins_or_tokens_reference():
    response = requests.get(
        url="{}tokens/reference".format(
            current_app.config["SERVER_API_BASE_URL"]
        ),
    )
    return response.json(), response.status_code


def get_projects():
    response = requests.get(
        url="{}projects".format(current_app.config["SERVER_API_BASE_URL"]),
    )
    return response.json(), response.status_code


def get_project_last_tweet(project):
    response = requests.get(
        url="{}projects/twitter/{}".format(
            current_app.config["SERVER_API_BASE_URL"], project
        ),
    )
    return response.json(), response.status_code
