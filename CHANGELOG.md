# Changelog
All changes will be registered here per release.

## [0.8.8] - Current data
Fix Binance status call.  
Code refactoring and fixes. 

## [0.8.7] - 2021-11-20
Added `Algorand / ALGO` Project/Token.  
Added `Dfinity / ICP` Project/Token.  
Added `BUSD` stable coin.  
Code refactoring and fixes. 

## [0.8.6] - 2021-07-03
Fixed `COINBASE` Exchange Rate limits that would result in an HTTP 429 Too Many Requests.  
Removed deprecated Projects that would make DB Migrations fail.  
Code refactoring and fixes. 

## [0.8.5] - 2021-03-22
Added Telegram group to landing page.
Code fixes and performance improvements. 

## [0.8.4] - 2020-12-26
Updated Landing page.  
Added Binance Exchange User Account connectivity.  
Added Spotlight Search.  
Added Keyboard shortcuts.  
Added `SNX`, `RLC` Projects/Tokens.  
Code fixes and performance improvements. 

## [0.8.3] - 2020-12-06
Added Coins/Tokens page.  
Added feature to list/show/mark Coins/Tokens as Favourites.  
Changed from `LEND` to `AAVE` Token.  
Added `USDT`, `USDC` and `DAI` Projects/Tokens.  
Added `DOT` and `NU` Projects/Tokens.  

## [0.8.2] - 2020-10-02
Added possibility of having N Market depth Charts per Coin/Token page through configuration.  
Added pair `EWT/USDT`.  
Client website is compliant with Open Graph Protocol.    
Code fixes and performance improvements. 

## [0.8.1] - 2020-08-23
Added Telegram alerts.  
Added `Fantom` Project and `FTM` Token.  
Added `Chainlink` Project and `LINK` Token.  
Added nginx configuration examples.  
Code fixes and improvements. 

## [0.7.0] - 2020-06-20
Improvements in Market Depth UI.  
Add exchange `Liquid` and `EWT` Token.  
`xt-tasks` service can now run the Tasks passed by argument and possible to setup different Celery Queues.  
Added `KNC`, `LEND` and `REN` Projects/Tokens.
Added Market Depth for all `IDEX` Exchange Pairs.  
Code fixes and improvements.  

## [0.6.0] - 2020-05-17
Added the following exchanges:

* Bitstamp
* Kucoin
* Coinbase Pro

Added Market Depth for all Binance Pairs.  
Code fixes and improvements.  

## [0.5.0] - 2020-05-04
Added Projects Coin or Token Wikipedia summary info with Twitter number of followers.  
Added Chart showing Project Twitter's data.  
Added Chart showing Tether data.  
Added Price change (10s, 1h, 1d, 1w, 4w) to lists.  
Code fixes and improvements.  

## [0.4.0] - 2020-04-19
Increased Coin/Token `Price Change Chart` from 6 to 12 points.  
Added `Docker` files and `docker-compose.yml` to run all services in containers.  
Added Captcha upon User SignIn and SignUp.  
Code fixes and improvements. 

## [0.3.0] - 2020-02-22
Added Crypto Fear & Greed Index and its chart in UI.  
Added new LTO Network Token Binance pairs.  
Added Hedera Hashgraph Token Binance pairs.  
Added Charts in Tools and per Coin or Token.  
Added Progress Bar for all XHR Requests.  
Code fixes and improvements.  

## [0.2.0] - 2020-12-25
Added Alerts/Notifications Management and Web Push Notifications.
Added Notifications Filtering.    
Added VeChain, Monero, Cardano and Icon Ticker coins.
Added CSRF client protection.  
Code fixes and improvements.  

## [0.1.9] - 2019-11-23
Big code refactoring.  
Added User Sessions.  
Added Transactions and Portfolio Management.  
Added Blueprints.  
Added Python Marshmallow and Swagger API UI.  
Code fixes and improvements.  

## [0.1.8] - 2019-10-16
Added UI Dark mode.  
UI Changes regarding the seconds ticker in Prices pages.  
Added Google Analytics.  

## [0.1.7] - 2019-08-21
Added new endpoint to see all pairs related with the given coin/token.  

## [0.1.6.1] - 2019-07-31
Code fix regarding CORS.      

## [0.1.6] - 2019-07-30
Added sparkline chart for each pair.    
Added Team and Donations sections in `README.md` file.  
Added Contact Form.  
Code fixes.  

## [0.1.5] - 2019-07-20
Added changes and improvements in UI.  
General Code fixes. 

## [0.1.4.1] - 2019-07-08
Added exchange:

* Binance DEX

Updated README.md.  
Code refactoring and code fixes.

## [0.1.3.1] - 2019-06-30
Added collection of data for any configured crypto-currency (coin or token) in 
the following exchanges:  

* Bitmax
* DCoin
* Bilaxy

Added Mongo data migrations capability.  
All tickers will always be updated each 10 seconds compared with 
referenced history ticker.  
Added pairs LTO/BTC, LTO/ETH and LTO/USDT in `settings_exchanges.py`.  
Setup and added testing to the whole framework.  
General Code fixes. 

## [0.1.3] - 2019-03-19
Added support for dev and prod (using eventlet and Gunicorn) environments when
running `xt-server` and `xt-client`.  
Added real-time active number of users in dashboard page.  
Added 6 more Tickers.  
Added adequate mongodb collection indexes to improve data fetching performance.  

## [0.1.2] - 2019-03-10
Code improvements related with project configuration.  

## [0.1.1.2] - 2019-03-10
Code fixes regarding sdist package.  

## [0.1.1.1] - 2019-03-03
Added menu in HTML templates to show tickers and pairs.  

## [0.1.1] - 2019-03-03
Beautified HTML templates.  
Code refactoring.  
Code fixes.  

## [0.1.0] - 2019-02-01
Updated HTML templates.  

## [0.0.9] - 2019-01-31
General Code fixes.  

## [0.0.8] - 2019-01-31
Refactored HTML templates and server API.  

## [0.0.7] - 2019-01-28
Built 3 web pages to show platform functionalities in the following URLs:  

* `/ticker/<exchange>/<pair>/<frequency>`
* `/ticker/<pair>/<frequency>`
* `/ticker/<frequency>`
* `/ticker`

## [0.0.6] - 2019-01-20
Added first working version of Web Server API and Web page.  
Implemented SocketIO.  
Added --version argument to display current version of the tool.  
Updated section Roadmap in `CHANGELOG.md`.  
Added more help in `README.md`.  

## [0.0.5] - 2018-12-22
Added command line help support.  
Added more help in `README.md`.  

## [0.0.4.1] - 2018-12-17
Fixed `README.md`.  

## [0.0.4] - 2018-12-16
Added collection of data for any configured crypto-currency (coin or token) in 
the following exchanges:  

* Bithumb
* Coinbene

Bug fixing.  
Changed `settings.py`.  
Published it on PyPI.  

## [0.0.3] - 2018-12-15
Added collection of data for any configured crypto-currency (coin or token) in 
the following exchanges:

* OkCoin

Added `MANIFEST.in`.  
Bug fixing.  

## [0.0.2] - 2018-12-07
Added `CHANGELOG.md` and corrected `README.md`.  

## [0.0.1] - 2018-12-05
Added collection of data for any configured crypto-currency (coin or token) in 
the following exchanges:  

* Binance
* Uphold
* OkEx
* Idex
* Bibox
* Switcheo
* Hotbit
