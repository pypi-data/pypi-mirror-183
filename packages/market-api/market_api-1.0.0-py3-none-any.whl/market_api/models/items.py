import datetime
import typing

import pydantic

from market_api.models.base import BaseResponse
from market_api.models.enum import *

__all__ = (
    'ItemsSearchByHashNameResponse',
    'ItemsSearchByHashNameSpecificResponse',
    'ItemsSearchListByHashNameAllResponse',
)


class SearchByHashNameItem(pydantic.BaseModel):
    market_hash_name: str
    price: int
    class_id: int = pydantic.Field(alias='class')
    instance_id: int = pydantic.Field(alias='instance')
    count: int


class ItemsSearchByHashNameResponse(BaseResponse):
    currency: Currency
    items: typing.List[SearchByHashNameItem] = pydantic.Field(alias='data')


class SearchByHashNameSpecificExtra(pydantic.BaseModel):
    float_value: typing.Optional[str] = pydantic.Field(alias='float')
    phase: typing.Optional[str]


class SearchByHashNameSpecific(pydantic.BaseModel):
    id: int
    market_hash_name: str
    price: int
    class_id: int = pydantic.Field(alias='class')
    instance_id: int = pydantic.Field(alias='instance')
    extra: SearchByHashNameSpecificExtra


class ItemsSearchByHashNameSpecificResponse(BaseResponse):
    currency: Currency
    data: typing.List[SearchByHashNameSpecific]


class SearchListByHashNameAllItemExtra(pydantic.BaseModel):
    asset: typing.Optional[int]
    float_value: typing.Optional[str] = pydantic.Field(alias='float')
    phase: typing.Optional[str]
    percent_success: typing.Optional[float]
    average_time: typing.Optional[float]


class SearchListByHashNameAllItem(pydantic.BaseModel):
    id: int
    price: int
    class_id: int = pydantic.Field(alias='class')
    instance_id: int = pydantic.Field(alias='instance')
    extra: SearchListByHashNameAllItemExtra


class ItemsSearchListByHashNameAllResponse(BaseResponse):
    currency: Currency
    data: typing.Dict[str, typing.List[SearchListByHashNameAllItem]]
