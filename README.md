# XTCryptoSignals

**XTCryptoSignals** is a Python service that collects crypto-currencies symbols 
pairs data such as BTC/USDT, ETH/BTC or any other pair that a Crypto-currency 
Exchange API supports and allows the user to setup **signals** based on rules 
to send real-time notifications through e-mail or Push Notifications to the 
browser or mobile app. It will allow as well automatic trading.


## Roadmap

* [x] Add crypto-currencies exchanges (Dec 2018)
* [ ] Setup notification rules (Dec 2018 / Jan 2019)
* [ ] Implement e-mail and web browser push notifications signals (Jan 2019)
* [ ] Start building Unit, functional and end-to-end testing (From Jan 2019)
* [ ] Implement automatic trading (Feb/Mar 2019)
* [ ] Build iOS app (Mar 2019)


## Getting Started

### Pre-requisites

* [Python 3.x](https://www.python.org/download/releases/3.0)
* [Redis](https://redis.io/download)
* [MongoDB](https://www.mongodb.com)


## Installation

### Install from source
Clone project repository
```bash
hg clone ssh://hg@bitbucket.org/pantunes/xtcryptosignals
cd xtcryptosignals
```

Setup Python virtual environment:
```bash
virtualenv venv -p python3
source venv/bin/activate
```

Install package
```bash
pip install -e .
```

(Dependencies will be installed automatically from 
[requirements.txt](requirements.txt))


### Install from PyPi
Create folder project:
```bash
mkdir <project directory>
cd <project directory>
```

Setup Python virtual environment:
```bash
virtualenv venv -p python3
source venv/bin/activate
```

Install package
```bash
pip install xtcryptosignals
```

(Dependencies will be installed automatically from 
[requirements.txt](requirements.txt))


## Start service

```bash
xt-crypto-signals
```

Starts standalone script without Celery (for testing purposes)
```bash
xt-crypto-signals-test
```

### Setup

There is already an initial setup with some crypto-currencies 
(coins and tokens) that can be changed in 
[settings_exchanges.py](xtcryptosignals/settings_exchanges.py).

```python
BIBOX: {
    'pairs': [
        ('ONT', 'USDT'),
        ('ONT', 'BTC'),
        ('ONT', 'ETH'),
        ('NEO', 'USDT'),
        ('NEO', 'BTC'),
        ('NEO', 'ETH'),
        ('LTC', 'USDT'),
        ('LTC', 'BTC'),
        ('CARD', 'ETH'),
    ]
}

UPHOLD: {
    'pairs': [
        ('BTC', 'USD'),
        ('ETH', 'USD'),
        ('LTC', 'USD'),
        ('XRP', 'USD'),
    ]
}
```

Initial setup to create dynamic MongoDB collections for data segmentation 
categorized by Exchanges pooling frequency in 
[settings.py](xtcryptosignals/settings.py).
```python
HISTORY_FREQUENCY = (
    '10s', '30s', '1m', '10m', '30m', '1h', '3h', '6h', '12h', '24h'
)
```

### Results
This service is fast as it uses threading.
It takes around 6 seconds to collect data of 70 crypto-currencies symbols pairs
from 7 exchanges and save it in 11 collections in MongoDB.
(Depending on external Exchange APIs availability and Internet 
connection/latency)

## Disclaimer
This project is work in progress and when it comes to trading use it at your 
own risk.


## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
