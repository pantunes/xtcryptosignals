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
            404:
                description: Sockets API is NOT OK
        """

        try:
            response = requests.get(
                f"http://{current_app.config['IP_ADDRESS']}:"
                f"{current_app.config['PORT']}/socket.io/?EIO=4"
            )
            status_code = response.status_code
            status_text = "OK"
        except Exception:
            status_code = 404
            status_text = "NOT OK"

        return dict(status=status_text), status_code


api.add_resource(StatusAPI, "/status/api")
api.add_resource(StatusSocketsAPI, "/status/api/sockets")
