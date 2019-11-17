__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import validate_io
from xtcryptosignals.server.api.contact import service
from xtcryptosignals.server.api.contact.schemas import ContactInputSchema


bp = Blueprint('contact', __name__)
api = Api(bp)


class ContactPost(Resource):
    @validate_io(schema_in=ContactInputSchema, is_form=True)
    def post(self, valid_data):
        """
        Submit contact form data
        ---
        tags:
            - User
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
            400:
                description: Error in input validation
            402:
                description: Invalid Form payload
        """
        service.save_contact(data=valid_data)


api.add_resource(ContactPost, '/contact')
