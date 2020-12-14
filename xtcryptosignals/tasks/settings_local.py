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
# Add the following Personal Exchange keys and secrets to a config file
# in order to interact with the Exchange using this platform.
#
# These keys and secrets should never be shared or commit in the
# remote repository. Only you should know them.
#
# It's very advisable to create a READ-ONLY API credentials in the
# Exchange.
#
# In case you wish the platform to post orders use it at your own risk.
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
