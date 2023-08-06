import typing

import aiohttp

__all__ = (
    'MarketException',
    'MarketNotSuccessException',
)


class MarketException(aiohttp.ClientError):

    def __init__(self, error: typing.Any):
        self.error = error


class MarketNotSuccessException(MarketException):
    ...
