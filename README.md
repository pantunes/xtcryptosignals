# XTCryptoSignals

**XTCryptoSignals** is a Python library that includes multiple services such as:
Data collection crypto-currencies coins and/or tokens symbols pairs data such as BTC/USDT, ETH/BTC or any other pair that a Crypto-currency Exchange API 
supports;
A **signals** service based on rules to send real-time notifications through e-mail or Push Notifications to the browser or mobile app;
And a service that enables automatic trading.


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
(Dependencies will be installed automatically from [requirements.txt](requirements.txt))

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

Install package:
```bash
pip install xtcryptosignals
```


## Start service

```bash
xt-crypto-signals
```

Starts standalone script without Celery (for testing purposes):
```bash
xt-crypto-signals --testing
```

To get a list of supported exchanges:
```bash
xt-crypto-signals --list-config exchanges

binance
uphold
okex
idex
switcheo
hotbit
bibox
okcoin
bithumb
coinbene
```
(Drop [me](mailto:pjmlantunes@gmail.com) an email if you want a new one to be supported or contribute to this project creating a pull request)

Command line help
```bash
xt-crypto-signals --help

Usage: xt-crypto-signals [OPTIONS]

  Use this tool to collect data from configured coins or/and tokens from
  configured crypto-currencies exchanges.

Options:
  --testing                       Execute this tool for 1 iteration for all
                                  configured coins and/or tokens. Not using
                                  Celery. (Useful for testing purposes)
  --list-config [exchanges|currencies]
                                  List 'exchanges' or 'currencies' (coins or
                                  tokens) per exchange that the tool currently
                                  supports.
  -h, --help                      Show this message and exit.
```

### Setup

There is already an initial setup with some crypto-currencies (coins and tokens) that can be added or/and removed in [settings_exchanges.py](xtcryptosignals/settings_exchanges.py).

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

Initial setup to create dynamic MongoDB collections for data segmentation categorized by Exchanges pooling frequency in [settings.py](xtcryptosignals/settings.py).
```python
HISTORY_FREQUENCY = (
    '10s', '30s', '1m', '10m', '30m', '1h', '3h', '6h', '12h', '24h'
)
```

### Results
This service is fast as it uses threading.
In my current system *(Macbook pro 2017)* it takes around 6 seconds to collect data of 70 crypto-currencies symbols pairs from 7 exchanges and save it in 11 collections in MongoDB.
(This performance figure depends on used hardware and Internet connection / latency)

## Disclaimer
This project is work in progress and when it comes to trading use it at your own risk.


## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
