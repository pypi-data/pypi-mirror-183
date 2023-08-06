# market-api

![PyPI](https://img.shields.io/pypi/v/market-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/market-api)
![GitHub](https://img.shields.io/github/license/lordralinc/market_api)
[![Downloads](https://pepy.tech/badge/market-api)](https://pepy.tech/project/market-api)


## Получение токена
[market.csgo.com](https://market.csgo.com/docs-v2)


## Использование

```python
import datetime
import pprint
from market_api import MarketConfig, MarketClient, MarketException, models

config = MarketConfig(api_key="...")
client = MarketClient(config)

pprint.pprint(await client.account.get_my_steam_id())
pprint.pprint(await client.account.change_currency(models.Currency.EUR))
pprint.pprint(
    await client.trades.history(
        datetime.datetime.now() - datetime.timedelta(days=1),
        datetime.datetime.now()
    )
)
async for message in client.wss.listen_raw(
    [models.WSSChannel.HISTORY_GO],
    need_auth=True
):
    pprint.pprint(message)
```
