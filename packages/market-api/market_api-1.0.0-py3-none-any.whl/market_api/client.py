import datetime
import enum
import logging
import time
import typing

import aiohttp
import orjson

from . import categories
from .const import __version__
from .exceptions import MarketNotSuccessException, MarketException
from .models import MarketConfig

__all__ = (
    'MarketClient',
)

logger = logging.getLogger('market_api.client')


class MarketClient:
    _session: typing.Optional[aiohttp.ClientSession]

    def __init__(self, config: MarketConfig):
        self.cfg = config
        self._session = None

        self.account = categories.AccountCategory(self)
        self.history = categories.HistoryCategory(self)
        self.items = categories.ItemsCategory(self)
        self.orders = categories.OrdersCategory(self)
        self.prices = categories.PricesCategory(self)
        self.trades = categories.TradesCategory(self)
        self.wss = categories.WSSCategory(self)

    @property
    def session(self):
        if not self._session or self._session.closed:
            self._session = aiohttp.ClientSession(
                headers={'User-Agent': f'market_api/{__version__}'},
                raise_for_status=True
            )
        return self._session

    async def close(self):
        if not self._session or self._session.closed:
            return
        await self._session.close()

    async def __aenter__(self) -> "MarketClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def _convert_param(self, value: typing.Any) -> typing.Any:
        if isinstance(value, bool):
            return int(value)
        elif isinstance(value, enum.Enum):
            return self._convert_param(value.value)
        elif isinstance(value, datetime.datetime):
            return int(value.timestamp())
        elif isinstance(value, list):
            new_list = []
            for item in value:
                new_list.append(self._convert_param(item))
            return new_list
        elif isinstance(value, dict):
            new_dict = {}
            for k, v in value.items():
                new_dict[k] = self._convert_param(v)
            return new_dict
        return value

    def _get_params(self, params: dict, need_auth: bool = True) -> typing.Sequence[typing.Tuple[str, typing.Any]]:
        new_params = []
        if need_auth:
            new_params.append(('key', self.cfg.api_key), )
        for key, value in params.items():
            new_value = self._convert_param(value)
            if isinstance(new_value, list):
                for item in new_value:
                    new_params.append((f'{key}[]', item,))
            else:
                new_params.append((key, new_value,))
        return [(k, v,) for k, v in new_params if v is not None]

    async def request(
            self,
            method: str,
            need_auth: bool = True,
            raw: bool = False,
            **params
    ):
        _params = self._get_params(params, need_auth)
        logger.debug(f"Send request to {method} with params {_params!r}")
        async with self.session.get(
                self.cfg.api_url + method,
                params=_params
        ) as response:
            json_response = await response.json(loads=orjson.loads)
            if raw:
                return json_response
            logger.debug(f"Response from {method} is {json_response!r}")
            if 'error' in json_response:
                raise MarketException(json_response['error'])
            if 'success' in json_response and not json_response['success']:
                raise MarketNotSuccessException(json_response)
            return json_response
