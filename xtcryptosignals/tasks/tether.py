__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import cfscrape
from bs4 import BeautifulSoup
from etherscan.tokens import Tokens
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.tasks.models.tether import Tether
from xtcryptosignals.tasks import settings as s


TETHER_CONTRACT_ADDRESS = "0xdac17f958d2ee523a2206206994597c13d831ec7"

URL = f"https://etherscan.io/token/{TETHER_CONTRACT_ADDRESS}"


def _get_tether_num_holders():
    scraper = cfscrape.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, "html.parser")

    try:
        selector = soup.find(id="ContentPlaceHolder1_tr_tokenHolders").find_all(
            "div"
        )[-1]
    except AttributeError:
        # @note: If fails, most likely CAPTCHA! > can't do anything to prevent it :-(
        return -1

    try:
        return int(
            selector.string.replace(".", "")
            .replace(",", "")
            .replace("addresses", "")
            .strip()
        )
    except AttributeError:
        # @note: HTML structure changed a bit recently
        pass

    try:
        # @note: Trying a bit differently...
        return int(
            selector.text.replace(".", "")
            .replace(",", "")
            .replace("addresses", "")
            .strip()
            .split()[0]
        )
    except AttributeError:
        pass

    # We can't get this one right
    return -1


@task(bind=True)
@use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
def update(self):
    logger = self.get_logger()

    try:
        api = Tokens(
            contract_address=TETHER_CONTRACT_ADDRESS,
            api_key=s.ETHERSCAN_API_KEY,
        )
        Tether(
            total_supply_eth=int(api.get_total_supply()) / 10 ** 6,
            num_holders_eth=_get_tether_num_holders(),
        ).save()

    except Exception as error:
        logger.error(f"tether error: {error}")
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
