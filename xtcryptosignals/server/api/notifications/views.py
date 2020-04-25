__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint, request
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import (
    validate_io,
    user_auth,
)
from xtcryptosignals.server.api.notifications import service
from xtcryptosignals.server.api.notifications.schemas import (
    NotificationRuleInputSchema,
    NotificationOutputSchema,
    NotificationRuleOutputSchema,
)

bp = Blueprint("notification", __name__)
api = Api(bp)


class NotificationRuleAdd(Resource):
    @validate_io(schema_in=NotificationRuleInputSchema)
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


class NotificationRuleEdit(Resource):
    @validate_io(schema_in=NotificationRuleInputSchema)
    @user_auth()
    def put(self, notification, auth, valid_data):
        """
        Edit Notification Rule
        ---
        tags:
            - Notifications
        security:
            - Bearer: []
        parameters:
            - name: notification
              in: path
              required: true
        responses:
            200:
                description: Changed Rule
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        return (
            service.edit_notification_rule(auth, notification, data=valid_data),
            200,
        )


class NotificationRuleGet(Resource):
    @validate_io(schema_out=NotificationRuleOutputSchema)
    @user_auth()
    def get(self, notification, auth):
        """
        Get Notification Rule
        ---
        tags:
            - Notifications
        security:
            - Bearer: []
        parameters:
            - name: notification
              in: path
              required: true
        responses:
            200:
                description: Changed Rule
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        return service.get_notification_rule(auth, notification), 200


class NotificationRuleDelete(Resource):
    @validate_io()
    @user_auth()
    def delete(self, notification, auth):
        """
        Delete Notification Rule
        ---
        tags:
            - Notifications
        security:
            - Bearer: []
        parameters:
            - name: notification
              in: path
              required: true
        responses:
            204:
                description: Deleted Rule
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        return service.delete_notification_rule(auth, notification), 204


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
        return (
            dict(
                notifications=service.notifications(
                    auth, coin_token=request.args.get("coin_token")
                ),
                coin_tokens=service.notification_coin_tokens(auth),
            ),
            200,
        )


class NotificationsRulesList(Resource):
    @validate_io(schema_out=NotificationRuleOutputSchema, many_out=True)
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


api.add_resource(NotificationRuleAdd, "/notifications/rule/add")
api.add_resource(NotificationRuleEdit, "/notifications/rule/<notification>")
api.add_resource(NotificationRuleGet, "/notifications/rule/<notification>")
api.add_resource(NotificationRuleDelete, "/notifications/rule/<notification>")
api.add_resource(NotificationsList, "/notifications")
api.add_resource(NotificationsRulesList, "/notifications/rules")
