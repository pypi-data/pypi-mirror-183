import datetime
import typing

import pydantic

from market_api.models.base import BaseResponse
from market_api.models.enum import *

__all__ = (
    'OrdersGetResponse',
    'OrdersSetResponse',
    'OrdersGetLogResponse',
)


class OrderItem(pydantic.BaseModel):
    hash_name: str
    phase: OrderPhase
    count: int
    date: datetime.datetime
    price: int
    currency: Currency
    partner: typing.Optional[int]
    token: typing.Optional[str]


class OrdersGetResponse(BaseResponse):
    orders: typing.List[OrderItem]


class OrdersSetResponse(BaseResponse):
    order: OrderItem


class OrderLogItem(pydantic.BaseModel):
    hash_name: str
    item_id: int
    created: datetime.datetime
    executed: datetime.datetime
    price: int
    currency: Currency


class OrdersGetLogResponse(BaseResponse):
    orders: typing.List[OrderLogItem]
