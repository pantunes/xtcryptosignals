__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import request, Blueprint
import xtcryptosignals.settings as s


bp = Blueprint('contact', __name__)


@bp.route('/contact', methods=['POST'])
def contact():
    r = requests.post(
        url='http://127.0.0.1:{}/contact'.format(s.PORT_SERVER),
        data=request.form,
    )
    return r.text, r.status_code
