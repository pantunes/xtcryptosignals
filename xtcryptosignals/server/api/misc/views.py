__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    Blueprint,
    current_app,
)
from flask_restful import Api, Resource


bp = Blueprint("status", __name__)
api = Api(bp)


class StatusAPI(Resource):
    def get(self):
        """
        Status of API
        ---
        tags:
            - Status
        security:
            - Bearer: []
        responses:
            200:
                description: API is OK
        """
        return dict(status="OK")


class StatusSocketsAPI(Resource):
    def get(self):
        """
        Status of Sockets API
        ---
        tags:
            - Status
        security:
            - Bearer: []
        responses:
            200:
                description: Sockets API is OK
        """
        response = requests.get(
            f"http://{current_app.config['IP_ADDRESS']}:"
            f"{current_app.config['PORT']}/socket.io/?EIO=4"
        )
        return dict(status="OK" if response.status_code == 200 else "NOT OK")


api.add_resource(StatusAPI, "/status/api")
api.add_resource(StatusSocketsAPI, "/status/api/sockets")
