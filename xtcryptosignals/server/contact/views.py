__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
from datetime import datetime
from flask import request, Blueprint
from flask_restful import Api, Resource


bp = Blueprint('contact', __name__)
api = Api(bp)


class ContactPost(Resource):
    def post(self):
        """
        Submit contact message
        ---
        tags:
            - Public
        parameters:
            - in: formData
              name: email
              type: string
              required: true
            - in: formData
              name: reason
              type: string
              required: true
            - in: formData
              name: message
              type: string
              required: true
        responses:
            200:
                description: Contact form was submitted successfully
        """
        with open(os.path.join('/tmp', 'contact.csv'), 'a') as f:
            f.write("{}\t{}\t{}\t{}\n".format(
                str(datetime.utcnow()),
                request.form.get('email', ''),
                request.form.get('reason', ''),
                request.form.get('message', '').replace(
                    '\r\n', ' '
                ).replace(
                    '\n', ' '
                ))
            )
        return dict(status='Ok')


api.add_resource(ContactPost, '/contact')
