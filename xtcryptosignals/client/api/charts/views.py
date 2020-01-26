__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    Blueprint,
    current_app,
)


bp = Blueprint('charts', __name__)


@bp.route('/charts/cfgi/btc', methods=['GET'])
def cfgi_btc():
    response = requests.get(
        url='{}charts/cfgi/btc'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
    )
    return response.json(), response.status_code
