__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import (
    Blueprint,
    abort,
    render_template,
    g,
)
from flask_wtf.csrf import CSRFError
from xtcryptosignals.client import service


bp = Blueprint('errors', __name__)


@bp.app_errorhandler(CSRFError)
def csrf_error(e):
    return dict(error=e.description), 400


@bp.app_errorhandler(401)
def unauthorized(_):
    return render_template(
        template_name_or_list='error.html',
        error='Unauthorized',
        frequency=g.HISTORY_FREQUENCY[0]
    ), 401


@bp.app_errorhandler(404)
def page_not_found(_):
    return render_template(
        template_name_or_list='error.html',
        error='The URL is incorrect'
    ), 404


@bp.app_errorhandler(408)
def unauthorized(_):
    return render_template(
        template_name_or_list='error.html',
        error="You've been logged out.",
        frequency=g.HISTORY_FREQUENCY[0]
    ), 408


@bp.before_request
def before_request():
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()


@bp.route('/errors/logged-out')
def logged_out():
    abort(408)
