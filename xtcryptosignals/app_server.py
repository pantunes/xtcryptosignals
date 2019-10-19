__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import xtcryptosignals.settings as s
from xtcryptosignals.server import create_app, socketio


app = create_app()


def main():
    """
    Start RESTFul server API and socketIO server.
    """
    import sys
    sys.argv = [sys.argv[0]]
    from flasgger import Swagger
    from xtcryptosignals.data_migrations import data_migrations_manager

    Swagger(app)

    data_migrations_manager.run()

    socketio.run(
        app=app,
        debug=s.DEBUG,
        use_reloader=s.DEBUG,
        host=s.IP_ADDRESS,
        port=s.PORT_SERVER,
    )
