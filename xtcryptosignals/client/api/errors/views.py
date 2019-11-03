__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint, abort
from flask import render_template
from xtcryptosignals import settings as s


bp = Blueprint('errors', __name__)


@bp.app_errorhandler(401)
def unauthorized(_):
    return render_template(
        template_name_or_list='error.html',
        error='Unauthorized',
        frequency=s.HISTORY_FREQUENCY[0]
    ), 401


@bp.app_errorhandler(404)
def page_not_found(_):
    return render_template(
        template_name_or_list='error.html',
        error='The URL is incorrect'
    ), 404


@bp.route('/errors/logged-out')
def logged_out():
    abort(401)
