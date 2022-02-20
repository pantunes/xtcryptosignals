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
from flask_login import current_user


def get_history_frequency():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}tokens/frequency",
    )
    return response.json(), response.status_code


def get_symbols_per_exchange():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}tokens/symbols",
    )
    return response.json(), response.status_code


def get_coins_or_tokens_reference():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}tokens/reference",
    )
    return response.json(), response.status_code


def get_coins_or_tokens_favourites():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}favourites",
        headers=dict(Authorization=current_user.id),
    )
    return response.json(), response.status_code


def get_projects():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}projects"
    )
    return response.json(), response.status_code


def get_project_last_tweet(project):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}projects/twitter/{project}"
    )
    return response.json(), response.status_code
