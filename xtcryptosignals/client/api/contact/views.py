__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    request,
    Blueprint,
    current_app,
)


bp = Blueprint('contact', __name__)


@bp.route('/contact', methods=['POST'])
def contact():
    response = requests.post(
        url='{}contact'.format(current_app.config['SERVER_API_BASE_URL']),
        data=request.form,
    )
    return response.text, response.status_code
