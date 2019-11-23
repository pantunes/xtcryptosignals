__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import timedelta


class Config(object):
    IP_ADDRESS = '0.0.0.0'

    PORT = 8000

    TESTING = False

    SECRET_KEY = None

    SERVER_API_BASE_URL = 'http://127.0.0.1:5000/'


class ConfigProduction(Config):
    DEBUG = False

    TEMPLATES_AUTO_RELOAD = False

    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    SESSION_PROTECTION = 'strong'


class ConfigDevelopment(Config):
    DEBUG = True

    TEMPLATES_AUTO_RELOAD = True

    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

    SESSION_PROTECTION = 'basic'
