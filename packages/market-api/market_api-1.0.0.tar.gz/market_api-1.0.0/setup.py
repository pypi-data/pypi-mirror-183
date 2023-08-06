# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['market_api', 'market_api.categories', 'market_api.models']

package_data = \
{'': ['*']}

install_requires = \
['aenum>=3.1.11,<4.0.0',
 'aiohttp>=3.8.3,<4.0.0',
 'orjson>=3.8.3,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'market-api',
    'version': '1.0.0',
    'description': 'market.csgo.com api v2 wrapper',
    'long_description': '# market-api\n\n![PyPI](https://img.shields.io/pypi/v/market-api)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/market-api)\n![GitHub](https://img.shields.io/github/license/lordralinc/market_api)\n[![Downloads](https://pepy.tech/badge/market-api)](https://pepy.tech/project/market-api)\n\n\n## Получение токена\n[market.csgo.com](https://market.csgo.com/docs-v2)\n\n\n## Использование\n\n```python\nimport datetime\nimport pprint\nfrom market_api import MarketConfig, MarketClient, MarketException, models\n\nconfig = MarketConfig(api_key="...")\nclient = MarketClient(config)\n\npprint.pprint(await client.account.get_my_steam_id())\npprint.pprint(await client.account.change_currency(models.Currency.EUR))\npprint.pprint(\n    await client.trades.history(\n        datetime.datetime.now() - datetime.timedelta(days=1),\n        datetime.datetime.now()\n    )\n)\nasync for message in client.wss.listen_raw(\n    [models.WSSChannel.HISTORY_GO],\n    need_auth=True\n):\n    pprint.pprint(message)\n```\n',
    'author': 'lordralinc',
    'author_email': 'lordralinc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lordralinc/market_api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
