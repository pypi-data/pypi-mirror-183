import pydantic
import typing

__all__ = (
    'MarketConfig',
)


class MarketConfig(pydantic.BaseModel):
    api_key: str
    wss_key: typing.Optional[str] = None
    wss_url: str = 'wss://wsn.dota2.net/wsn/'
    api_url: str = 'https://market.csgo.com/api/v2/'
