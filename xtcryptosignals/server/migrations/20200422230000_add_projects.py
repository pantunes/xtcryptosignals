__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

from xtcryptosignals.server.migrations import AddProjectMigration


class Migration(AddProjectMigration):
    PROJECTS = dict(
        ADA=dict(
            name="Cardano",
            website="https://www.cardano.org",
            twitter="https://twitter.com/cardano",
            wikipedia=None,
        ),
        BNB=dict(
            name="Binance",
            website="https://binance.com",
            twitter="https://twitter.com/binance",
            wikipedia="https://en.wikipedia.org/wiki/Binance",
        ),
        BTC=dict(
            name="Bitcoin",
            website="https://bitcoin.org",
            twitter="https://twitter.com/Bitcoin",
            wikipedia="https://en.wikipedia.org/wiki/Bitcoin",
        ),
        ETH=dict(
            name="Ethereum",
            website="https://ethereum.org",
            twitter="https://twitter.com/Ethereum",
            wikipedia="https://en.wikipedia.org/wiki/Ethereum",
        ),
        HBAR=dict(
            name="Hedera Hashgraph",
            website="https://www.hedera.com",
            twitter="https://twitter.com/hashgraph",
            wikipedia="https://en.wikipedia.org/wiki/Hashgraph",
        ),
        ICX=dict(
            name="Icon",
            website="https://icon.foundation",
            twitter="https://twitter.com/helloiconworld",
            wikipedia=None,
        ),
        LTC=dict(
            name="Litecoin",
            website="https://litecoin.org",
            twitter="https://twitter.com/litecoin",
            wikipedia="https://en.wikipedia.org/wiki/Litecoin",
        ),
        LTO=dict(
            name="LTO Network",
            website="https://www.ltonetwork.com",
            twitter="https://twitter.com/LTOnetwork",
            wikipedia=None,
        ),
        XNO=dict(
            name="Nano",
            website="https://nano.org",
            twitter="https://twitter.com/nano",
            wikipedia="https://en.wikipedia.org/wiki/Nano_(cryptocurrency)",
        ),
        ONT=dict(
            name="Ontology",
            website="https://ont.io",
            twitter="https://twitter.com/OntologyNetwork",
            wikipedia=None,
        ),
        VET=dict(
            name="VeChain",
            website="https://www.vechain.org",
            twitter="https://twitter.com/vechainofficial",
            wikipedia="https://en.wikipedia.org/wiki/Ven_(currency)",
        ),
        XLM=dict(
            name="Stellar",
            website="https://www.stellar.org",
            twitter="https://twitter.com/stellarorg",
            wikipedia="https://en.wikipedia.org/wiki/Stellar_(payment_network)",
        ),
        XMR=dict(
            name="Monero",
            website="https://www.getmonero.org",
            twitter="https://twitter.com/monero",
            wikipedia="https://en.wikipedia.org/wiki/Monero_(cryptocurrency)",
        ),
        XRP=dict(
            name="Ripple",
            website="https://ripple.com",
            twitter="https://twitter.com/Ripple",
            wikipedia="https://en.wikipedia.org/wiki/Ripple_(payment_protocol)",
        ),
        XTZ=dict(
            name="Tezos",
            website="https://tezos.com",
            twitter="https://twitter.com/tezos",
            wikipedia="https://en.wikipedia.org/wiki/Tezos",
        ),
    )
