__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from redis import Redis
from xtcryptosignals import (
    __title__,
    __version__,
    __description__,
)


class Config(object):
    IP_ADDRESS = '0.0.0.0'

    PORT = 5000

    TESTING = False

    BROKER_URL = 'redis://localhost:6379'

    SESSION_TYPE = 'redis'

    SESSION_REDIS = Redis.from_url(BROKER_URL)

    SECRET_KEY = None

    CORS_ALLOWED_ORIGINS = None


class ConfigProduction(Config):
    DEBUG = False

    SESSION_COOKIE_SECURE = True


class ConfigDevelopment(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False

    SWAGGER = {
        "info": {
            "title": __title__,
            "version": __version__,
            "description": __description__,
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        },
        "specs": [
            {
                "endpoint": 'apispec_xtcryptosignals',
                "route": '/apispec_xtcryptosignals.json',
            }
        ],
    }
