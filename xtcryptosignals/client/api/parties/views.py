__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import Blueprint


bp = Blueprint('parties', __name__)


@bp.route('/parties/fear-and-greed-index', methods=['GET'])
def fear_and_greed_index():
    response = requests.get(url='https://api.alternative.me/fng')
    return dict(response.json())
