import datetime
import typing

import pydantic

from market_api.models.base import BaseResponse
from market_api.models.enum import *

__all__ = (
    'AccountGetMoneyResponse',
    'AccountGetMySteamIDResponse',
    'AccountMoneySendResponse',
    'AccountMoneySendHistoryResponse',
    'AccountSetTradeTokenResponse',
)


class AccountGetMoneyResponse(BaseResponse):
    currency: Currency
    money: float


class AccountGetMySteamIDResponse(BaseResponse):
    steamid32: int
    steamid64: int


class AccountMoneySendResponse(BaseResponse):
    from_id: int = pydantic.Field(alias='from')
    to_id: int = pydantic.Field(alias='to')
    amount: int


class AccountMoneySendItem(pydantic.BaseModel):
    id: int
    from_id: int = pydantic.Field(alias='from')
    to_id: int = pydantic.Field(alias='to')
    amount_from: int
    currency_from: Currency
    amount_to: int
    currency_to: Currency


class AccountMoneySendHistoryResponse(BaseResponse):
    data: typing.List[AccountMoneySendItem]


class AccountSetTradeTokenResponse(BaseResponse):
    token: str

