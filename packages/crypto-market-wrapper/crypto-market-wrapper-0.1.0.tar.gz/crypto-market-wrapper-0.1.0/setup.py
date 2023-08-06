# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crypto_market_wrapper']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'crypto-market-wrapper',
    'version': '0.1.0',
    'description': '',
    'long_description': 'Welcome to the crypto_market_wrapper package! This package allows users to retrieve various types of data about cryptocurrency listed on the Binance exchange. \n\nWith this package, users can access:\n\n- Recent Trades List\n- Aggregate Trades List\n- Candlestick Data\n- UIKlines data\n- Current Average Price\n- 24hr Ticker Price Change Statistics\n- Symbol Order Book Ticker\n\n#### Install\n\n```\npip install crypto_market_wrapper\n```\n\n\n#### Import\n\n```\nfrom crypto_market_wrapper import crypto\n```\n\n##### Symbols\n\nThe function provides a DataFrame of valid cryptocurrency symbols.\n\n    Returns:\n        DataFrame: Symbols\n\n```\ncrypto.GET_SYMBOLS()\n```\n\n##### Recent Trades List\n\nThe function provides a DataFrame containing a list of recent trades.\n\n    Args:\n        SYMBOL (str, optinal): Defaults to "BTCUSDT"\n\n    Returns:\n        DataFrame: Recent Trades List\n\n```\ncrypto.GET_RECENT_TRADES_LIST()\n```\n\n##### Aggregate Trades List\n\nThe function provides a DataFrame containing an aggregate list of trades\n\n    Args:\n        SYMBOL (str, optinal): Defaults to "BTCUSDT".\n\n    Returns:\n        DataFrame: Aggregate Trades List\n\n```\ncrypto.GET_AGGREGATE_TRADES_LIST()\n```\n\n#### Candlestick Data\n\n The function provides a DataFrame containing candlestick data.\n\n    Args:\n        SYMBOL (str, optinal): Defaults to "BTCUSDT".\n        INTERVAL (str, optinal): Defaults to "1h".(\'1s\',\'1m\',\'3m\',\'5m\',\'15m\',\'30m\',\'1h\',\'2h\',\'4h\',\'6h\',\'8h\',\'12h\',\'1d\',\'3d\',\'1w\',\'1M\')\n        LIMIT (int, optional): A valid symbol is required(1000). Defaults to 500.\n\n    Returns:\n        DataFrame: Candlestick Data\n    \n```\ncrypto.GET_CANDLESTICK_DATA()\n```\n\n#### UIKlines data\n\nThe function provides a DataFrame containing candlestick data.\n\n    Args:\n        SYMBOL (str, optional): Defaults to "BTCUSDT".\n        INTERVAL (str, optional): Defaults to "1h".(\'1s\',\'1m\',\'3m\',\'5m\',\'15m\',\'30m\',\'1h\',\'2h\',\'4h\',\'6h\',\'8h\',\'12h\',\'1d\',\'3d\',\'1w\',\'1M\')\n        LIMIT (int, optional):  A valid limit is required(1000). Defaults to 500.\n\n    Returns:\n        DataFrame: UIKlines\n\n```\ncrypto.GET_UIKLINES()\n```\n\n\n#### Current Average Price\n\nThe function provides a dictionary containing the current average price\n\n    Args:\n        SYMBOL (str, optinal): Defaults to "BTCUSDT".\n\n    Returns:\n        Dict: Current Average Price\n\n```\ncrypto.GET_CURRENT_AVERAGE_PRICE()\n```\n\n#### 24hr Ticker Price Change Statistics\n\nThe function provides a DataFrame containing 24-hour ticker price change statistics.\n\n    Args:\n        SYMBOLS (list, optional): A valid symbol is required. Defaults to ["BTCUSDT"].\n\n    Returns:\n        DataFrame: 24hr Ticker Price Change Statistics\n\n```\ncrypto.GET_TICKER_PRICE_CHANGE_24H()\n```\n\n\n#### Symbol Order Book Ticker\n\nThe function provides a DataFrame containing order book ticker data.\n\n    Args:\n        SYMBOLS (list, optional): Defaults to ["BTCUSDT"].\n\n    Returns:\n        DataFrame: Order Book Ticker\n\n```\ncrypto.GET_SYMBOL_ORDER_BOOK_TICKER()\n```\n\n',
    'author': 'hasindusithmin',
    'author_email': 'hasindusithmin64@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hasindusithmin/crypto-market-wrapper.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
