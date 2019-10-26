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

    DEBUG = False
    TESTING = False

    SECRET_KEY = None


class ConfigProduction(Config):
    SERVER_API_BASE_URL = 'https://api.xtcryptosignals.com/'


class ConfigDevelopment(Config):
    DEBUG = True

    TEMPLATES_AUTO_RELOAD = True

    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    SERVER_API_BASE_URL = 'http://127.0.0.1:5000/'
