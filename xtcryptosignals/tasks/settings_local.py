__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from environs import Env


env = Env()
env.read_env(env("SETTINGS_APP"), recurse=False)


##############################################################################
# WARNING! WARNING! WARNING! WARNING! WARNING! WARNING! WARNING! WARNING!    #
##############################################################################
#
# @note: Do not add real credentials of each Exchange as the
# following data is used to instanciate a READ-ONLY client.
#
##############################################################################
# WARNING! WARNING! WARNING! WARNING! WARNING! WARNING! WARNING! WARNING!    #
##############################################################################

BINANCE_API_KEY = env.str("BINANCE_API_KEY", "")
BINANCE_API_SECRET = env.str("BINANCE_API_SECRET", "")

KUCOIN_API_KEY = env.str("KUCOIN_API_KEY", "")
KUCOIN_API_SECRET = env.str("KUCOIN_API_SECRET", "")
KUCOIN_API_PASSPHRASE = env.str("KUCOIN_API_PASSPHRASE", "")

IDEX_API_KEY = env.str("IDEX_API_KEY", "")
IDEX_ADDRESS = env.str("IDEX_ADDRESS", "")
IDEX_PRIVATE_KEY = env.str("IDEX_PRIVATE_KEY", "")
