# XTCryptoSignals

**XTCryptoSignals** is a Python service that collects crypto-currencies symbols 
pairs data such as BTC/USDT, ETH/BTC or any other pair that a Crypto-currency 
Exchange API supports and allows the user to setup **signals** based on rules 
to send real-time notifications through e-mail or Push Notifications to the 
browser or mobile app. It will allow as well automatic trading.


## Roadmap

* Setup notification rules (Dec 2018)
* Implement e-mail and push notifications (Dec 2018)
* Implement automatic trading (Jan 2019)
* Build iOS app (Feb 2019)


## Getting Started

### Pre-requisites

* [Python 3.x](https://www.python.org/download/releases/3.0)
* [Redis](https://redis.io/download)
* [MongoDB](https://www.mongodb.com)


## Install from source
```bash
hg clone ssh://hg@bitbucket.org/pantunes/xtcryptosignals
cd xtcryptosignals
```

Create Python virtualenv:
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

## Start service

```bash
xt-crypto-signals
```

Starts standalone script without Celery (for testing purposes)
```bash
xt-crypto-signals-test
```

### Setup

The library has some initial setup of crypto-currencies that can be changed 
in the file [settings_exchanges.py](settings_exchanges.py).

Examples:
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

## Disclaimer
 This project is work in progress and when it comes to trading use it at your 
 own risk.


## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
