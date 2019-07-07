__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

import xtcryptosignals.settings as s
from xtcryptosignals.server.views import socketio
from xtcryptosignals.server.views import app


def main():
    """
    Start RESTFul server API and socketIO server.
    """
    import sys
    sys.argv = [sys.argv[0]]
    from xtcryptosignals.data_migrations import data_migrations_manager

    data_migrations_manager.run()

    socketio.run(
        app,
        debug=s.DEBUG,
        use_reloader=s.DEBUG,
        host=s.IP_ADDRESS,
        port=s.PORT_SERVER,
    )
