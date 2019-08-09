# Changelog
All changes will be registered here per release.

## [0.1.7] - Current date
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

* /ticker/<exchange>/<pair>/<frequency>
* /ticker/<pair>/<frequency>
* /ticker/<frequency>
* /ticker

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
