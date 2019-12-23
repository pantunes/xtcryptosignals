__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
    g,
)
from flask_login import (
    login_required,
    current_user,
)
from xtcryptosignals.client import service
from xtcryptosignals import __version__
from xtcryptosignals.common.utils import (
    get_pairs,
    get_coin_tokens,
)


bp = Blueprint('notification', __name__)


@bp.context_processor
def context_processor():
    return dict(
        application_server_key=current_app.config['APPLICATION_SERVER_KEY'],
        socket_base_url=current_app.config['SOCKET_BASE_URL'],
        version=__version__,
        ga_tracking_id=current_app.config['GA_TRACKING_ID'],
        frequencies=g.HISTORY_FREQUENCY,
        pairs=get_pairs(g.SYMBOLS_PER_EXCHANGE),
        tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE),
    )


@bp.route('/notifications', methods=['GET'])
@login_required
def index():
    g.SYMBOLS_PER_EXCHANGE, _ = service.get_symbols_per_exchange()
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()
    return render_template(
        template_name_or_list='notification.html',
        frequency=g.HISTORY_FREQUENCY[0]
    )


@bp.route('/notifications/list', methods=['GET'])
@login_required
def notifications():
    response = requests.get(
        url='{}notifications'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
        headers=dict(Authorization=current_user.id),
        params=request.args,
    )
    return dict(results=response.json()), response.status_code


@bp.route('/notifications/rules', methods=['GET'])
@login_required
def rules():
    response = requests.get(
        url='{}notifications/rules'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
        headers=dict(Authorization=current_user.id),
    )
    return dict(results=response.json()), response.status_code


@bp.route('/notifications/rule/add', methods=['POST'])
@login_required
def rule_add():
    response = requests.post(
        url='{}notifications/rule/add'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
        headers=dict(Authorization=current_user.id),
        json=request.form.to_dict()
    )
    return response.json(), response.status_code
