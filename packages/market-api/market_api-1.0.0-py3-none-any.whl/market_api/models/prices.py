import datetime
import typing

import pydantic

from market_api.models import Currency
from market_api.models.base import BaseResponse

__all__ = (
    'PricesResponse',
    'PricesClassInstanceResponse',
)


class PricesItem(pydantic.BaseModel):
    market_hash_name: str
    volume: int
    price: float


class PricesResponse(BaseResponse):
    time: datetime.datetime
    currency: Currency
    items: typing.List[PricesItem]


class PricesClassInstanceItem(pydantic.BaseModel):
    price: float
    buy_order: float
    market_hash_name: str
    avg_price: typing.Optional[float]
    popularity_7d: typing.Optional[int]
    ru_name: typing.Optional[str]
    ru_rarity: typing.Optional[str]
    ru_quality: typing.Optional[str]
    text_color: typing.Optional[str]
    bg_color: typing.Optional[str]


class PricesClassInstanceResponse(BaseResponse):
    time: datetime.datetime
    currency: Currency
    items: typing.Dict[str, PricesClassInstanceItem]
