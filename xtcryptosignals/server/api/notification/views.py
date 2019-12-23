__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint, request
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import (
    validate_io,
    user_auth,
)
from xtcryptosignals.server.api.notification import service
from xtcryptosignals.server.api.notification.schemas import (
    NotificationRuleAddInputSchema,
    NotificationOutputSchema,
    NotificationRulesOutputSchema,
)

bp = Blueprint('notification', __name__)
api = Api(bp)


class NotificationRuleAdd(Resource):
    @validate_io(schema_in=NotificationRuleAddInputSchema)
    @user_auth()
    def post(self, auth, valid_data):
        """
        Add Notification Rule
        ---
        tags:
            - Notifications
        security:
            - Bearer: []
        responses:
            200:
                description: Added Rule
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        return service.add_notification_rule(auth, data=valid_data), 201


class NotificationsList(Resource):
    @validate_io(schema_out=NotificationOutputSchema)
    @user_auth()
    def get(self, auth):
        """
        Get list of Notifications
        ---
        tags:
            - Notifications
        security:
            - Bearer: []
        responses:
            200:
                description: Returned list of Notifications
            400:
                description: Error in session validation
            401:
                description: Unauthorized
            415:
                description: Error in output pre-validation
            416:
                description: Error in output validation
        """
        return dict(
            notifications=service.notifications(
                auth, coin_token=request.args.get('coin_token')
            ),
            coin_tokens=service.notification_coin_tokens(auth)
        ), 200


class NotificationsRulesList(Resource):
    @validate_io(schema_out=NotificationRulesOutputSchema, many_out=True)
    @user_auth()
    def get(self, auth):
        """
        Get list of Notification's Rules
        ---
        tags:
            - Notifications
        security:
            - Bearer: []
        responses:
            200:
                description: Returned list of Notification's Rules
            400:
                description: Error in session validation
            401:
                description: Unauthorized
            415:
                description: Error in output pre-validation
            416:
                description: Error in output validation
        """
        return service.notification_rules(auth), 200


api.add_resource(NotificationRuleAdd, '/notifications/rule/add')
api.add_resource(NotificationsList, '/notifications')
api.add_resource(NotificationsRulesList, '/notifications/rules')
