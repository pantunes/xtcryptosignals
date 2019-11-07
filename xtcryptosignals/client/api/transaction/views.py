__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint
from flask_login import login_required


bp = Blueprint('transaction', __name__)


@bp.route('/transactions', methods=['GET'])
@login_required
def index():
    return {'results': 'OK!'}
