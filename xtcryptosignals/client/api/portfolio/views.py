__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import (
    Blueprint,
    render_template,
    current_app,
)
from flask_login import (
    login_required,
)
from xtcryptosignals import settings as s
from xtcryptosignals import __version__
from xtcryptosignals.client.utils import (
    get_pairs,
    get_tokens,
)


bp = Blueprint('portfolio', __name__)


@bp.context_processor
def before_request():
    return dict(
        server_api_base_url=current_app.config['SERVER_API_BASE_URL'],
        version=__version__,
        ga_tracking_id=current_app.config['GA_TRACKING_ID'],
        frequencies=s.HISTORY_FREQUENCY,
        pairs=get_pairs(),
        tokens=get_tokens(),
        attributes=['Price'],
    )


@bp.route('/portfolio/<frequency>', methods=['GET'])
@login_required
def index(frequency):
    return render_template(
        template_name_or_list='portfolio.html',
        frequency=frequency,
    )
