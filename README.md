# XTCryptoSignals

**XTCryptoSignals** is a Python service that collects symbols pairs data such as BTC/USDT, ETH/BTC or any other pair that a Cryptocurrency Exchange API supports and allows the user to setup **signals** based on rules to send real-time notifications through e-mail or Push Notifications to the browser or mobile app.


## Roadmap

* Setup notification rules (Dec 2018)
* Implement automatic trading (Jan 2019)
* Build iOS app (Feb 2019)


## Getting Started

### Install from source
```bash
hg clone ssh://hg@bitbucket.org/pantunes/xtcryptosignals
cd xtcryptosignals
```

Create Python virtualenv:
```bash
virtualenv venv -p python3
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Install
```bash
pip install -e .
```

### Start service
```bash
. run.sh
```


## Disclaimer
 This project is work in progress and when it comes to trading use it at your own risk.


## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
