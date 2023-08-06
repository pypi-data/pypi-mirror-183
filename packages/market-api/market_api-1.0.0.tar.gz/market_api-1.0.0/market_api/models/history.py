import datetime
import typing

import pydantic

from market_api.models.base import BaseResponse
from market_api.models.enum import *

__all__ = (
    'HistoryCheckinResponse',
    'HistoryCheckoutResponse'
)


class CheckinItem(pydantic.BaseModel):
    """
    :ivar amount: Целое число, сумма с копейками/центами,
                    например 100 руб. = 10000 (2 знака копеек),
                    $10 (10€) = 10000 (3 знака у центов)
    """
    id: int
    uid: int
    system: str
    amount: int
    created: datetime.datetime
    currency: Currency


class HistoryCheckinResponse(BaseResponse):
    data: typing.List[CheckinItem]


class CheckoutItem(pydantic.BaseModel):
    """
    :ivar summ: Целое число, сумма с копейками/центами,
                    например 100 руб. = 10000 (2 знака копеек),
                    $10 (10€) = 10000 (3 знака у центов)
    :ivar paid: Целое число, сумма с копейками/центами,
                    например 100 руб. = 10000 (2 знака копеек),
                    $10 (10€) = 10000 (3 знака у центов)
    """
    id: int
    uid: int
    summ: int
    paid: int
    method: str
    wm: str
    system: typing.Optional[str]
    status: OperationHistoryStatus
    comment: str
    created: datetime.datetime
    currency: Currency
    can_cancel: bool


class HistoryCheckoutResponse(BaseResponse):
    data: typing.List[CheckoutItem]
