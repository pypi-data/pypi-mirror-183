import datetime
import typing

import pydantic

from market_api.models.base import BaseResponse
from market_api.models.enum import *

__all__ = (
    'TradesTradeRequestTakeResponse',
    'TradesTradeRequestGiveResponse',
    'TradesTradeRequestGiveP2PResponse',
    'TradesTradeRequestGiveP2PAllResponse',
    'TradesRemoveAllFromSaleResponse',
    'TradesItemsResponse',
    'TradesAddToSaleResponse',
    'TradesMyInventoryResponse',
    'TradesTradesResponse',
    'TradesBuyResponse',
    'TradesGetBuyInfoByCustomIDResponse',
    'TradesGetListBuyInfoByCustomIDResponse',
    'TradesHistoryResponse',
    'TradesOperationHistoryResponse',
    'TradesTestResponse',
    'TradesGetListItemsInfoResponse',
)


class TradesTradeRequestTakeResponse(BaseResponse):
    trade: int
    nick: str
    bot_id: int = pydantic.Field(alias='botid')
    profile: str
    secret: str
    items: typing.List[str]


class TradesTradeRequestGiveResponse(BaseResponse):
    trade: int
    nick: str
    bot_id: int = pydantic.Field(alias='botid')
    profile: str
    secret: str
    items: typing.List[int]


class TradesTradeRequestGiveP2POfferItem(pydantic.BaseModel):
    app_id: int = pydantic.Field(alias='appid')
    context_id: int = pydantic.Field(alias='contextid')
    asset_id: int = pydantic.Field(alias='assetid')
    amount: int = pydantic.Field(alias='amount')


class TradesTradeRequestGiveP2POffer(pydantic.BaseModel):
    partner: int
    token: str
    trade_offer_message: str = pydantic.Field(alias='tradeoffermessage')
    items: typing.List[TradesTradeRequestGiveP2POfferItem]


class TradesTradeRequestGiveP2PResponse(BaseResponse):
    hash: str
    offer: TradesTradeRequestGiveP2POffer


class TradesTradeRequestGiveP2PAllResponse(BaseResponse):
    hash: str
    offers: typing.List[TradesTradeRequestGiveP2POffer]


class TradesAddToSaleResponse(BaseResponse):
    item_id: int


class TradesItemsItem(pydantic.BaseModel):
    """
    :ivar item_id:   ID предмета в нашей системе.
    :ivar price:     Ваша цена.
    :ivar position:  Позиция в очереди продажи (сортировка по наименьшей цене),
                    в момент покупки выбирается самый дешевый предмет.
    :ivar bot_id:    ID бота, на котором находится предмет в статусе 4.
    :ivar asset_id:  ID предмета в инвентаре бота.
    :ivar left:      Времени осталось на передачу предмета,
                    после этого операция будет отменена и деньги вернутся
                    покупателю. Будут начислены штрафные баллы.
    """
    item_id: int
    asset_id: int = pydantic.Field(alias='assetid')
    class_id: int = pydantic.Field(alias='classid')
    instance_id: int = pydantic.Field(alias='instanceid')
    real_instance: int
    market_hash_name: str
    position: str
    price: int
    currency: Currency
    status: ItemStatus
    live_time: int
    left: typing.Optional[int]
    bot_id: typing.Optional[int] = pydantic.Field(alias='botid')


class TradesItemsResponse(BaseResponse):
    items: typing.List[TradesItemsItem]


class TradesRemoveAllFromSaleResponse(BaseResponse):
    """
    :ivar count: Количество предметов, которые были сняты с продажи, 0 если нет выставленных предметов.
    """
    count: int


class TradesMyInventoryItem(pydantic.BaseModel):
    """
    :ivar id:           ID (`asset_id`) для выставления на продажу (см. метод `trades.add_to_sale`).
    :ivar market_price: Рекомендованная цена продажи.
    """
    id: int
    class_id: int = pydantic.Field(alias='classid')
    instance_id: int = pydantic.Field(alias='instanceid')
    market_hash_name: str
    market_price: float
    tradable: int


class TradesMyInventoryResponse(BaseResponse):
    items: typing.List[TradesMyInventoryItem]


class TradesTradesItem(pydantic.BaseModel):
    """
    :ivar dir:      Направление трейда
    :ivar trade_id: SteamID трейд оффера
    :ivar bot_id:   SteamID нашего бота, который отправил его
    """
    dir: TradesTradesItemDirection
    trade_id: int
    bot_id: int
    timestamp: datetime.datetime


class TradesTradesItemFullListItemID(pydantic.BaseModel):
    id: int
    asset_id: int = pydantic.Field(alias='assetid')
    class_id: int = pydantic.Field(alias='classid')
    instance_id: int = pydantic.Field(alias='instanceid')


class TradesTradesItemFull(TradesTradesItem):
    secret: typing.Optional[str]
    nick: typing.Optional[str] = pydantic.Field(alias='nik')
    list_item_id: typing.Optional[typing.Dict[str, TradesTradesItemFullListItemID]]


class TradesTradesResponse(BaseResponse):
    trades: typing.List[TradesTradesItemFull]


class TradesBuyResponse(BaseResponse):
    """
    :ivar id: ID предмета
    """
    id: int


class TradesGetBuyInfoByCustomIDData(pydantic.BaseModel):
    """
    :ivar trade_id:     ID активного `trade_offer`
    :ivar steam_id_for: `Steamid(32)` кому передан предмет (если покупка был через метод `trades.buy[for]`)
    :ivar paid:         По чем была куплена вещь
    :ivar time:         Unix Timestamp когда была куплена вещь
    """
    item_id: int
    market_hash_name: str
    class_id: int = pydantic.Field(alias='classid')
    instance: int
    time: datetime.datetime
    # Пасиба великолепным докам с великолепными тайпингами
    send_until: typing.Optional[typing.Any]
    stage: BuyInfoStage
    paid: float
    causer: typing.Optional[typing.Any]
    currency: Currency
    steam_id_for: typing.Optional[int] = pydantic.Field(alias='for')
    trade_id: typing.Optional[int]


class TradesGetBuyInfoByCustomIDResponse(BaseResponse):
    data: TradesGetBuyInfoByCustomIDData


class TradesGetListBuyInfoByCustomIDResponse(BaseResponse):
    data: typing.Dict[str, TradesGetBuyInfoByCustomIDData]


class TradesHistoryItem(pydantic.BaseModel):
    """
    :ivar app: на какой площадке был куплен предмет
    :ivar for_steam_id: ID пользотвателя кому он был передан
    """

    item_id: int
    market_hash_name: str
    class_id: int = pydantic.Field(alias='class')
    instance_id: int = pydantic.Field(alias='instance')
    time: datetime.datetime
    event: Event
    app: Apps
    stage: BuyInfoStage
    for_steam_id: typing.Optional[int] = pydantic.Field(alias='for')
    custom_id: typing.Optional[str]
    paid: typing.Optional[int]
    currency: Currency


class TradesHistoryResponse(BaseResponse):
    data: typing.List[TradesHistoryItem]


class TradesOperationHistoryItem(pydantic.BaseModel):
    time: datetime.datetime
    event: Event
    currency: Currency

    # sell
    item_id: typing.Optional[int]
    market_hash_name: typing.Optional[str]
    class_id: typing.Optional[int] = pydantic.Field(alias='class')
    instance_id: typing.Optional[int] = pydantic.Field(alias='instance')
    price: typing.Optional[int]
    received: typing.Optional[int]
    stage: typing.Optional[BuyInfoStage]
    for_steam_id: typing.Optional[int] = pydantic.Field(alias='for')
    custom_id: typing.Optional[str]
    app: typing.Optional[Apps]

    # buy
    paid: typing.Optional[int]

    # checkout
    id: typing.Optional[int]
    amount: typing.Optional[int]
    status: typing.Optional[OperationHistoryStatus]


class TradesOperationHistoryResponse(BaseResponse):
    data: typing.List[TradesOperationHistoryItem]


class TradesTestStatus(pydantic.BaseModel):
    """
    :ivar user_token:         Установлена ли трейд ссылка
    :ivar trade_check:        Пройдена ли проверка доступности трейд офферов - https://market.csgo.com/check/
    :ivar site_online:        Находитесь ли Вы в онлайне на сайте ping
    :ivar site_notmpban:      Индикатор отсутствия бана за не передачу проданных вещей (на сутки)
    :ivar steam_web_api_key:  Установлен API ключ steam (нужен для продажи через p2p)
    """
    user_token: bool
    trade_check: bool
    site_online: bool
    site_notmpban: bool
    steam_web_api_key: bool


class TradesTestResponse(BaseResponse):
    status: TradesTestStatus


class TradesGetListItemsInfoData(pydantic.BaseModel):
    """   
    :ivar max:      max price
    :ivar min:      min price
    :ivar history:  sales history

    """
    max: int
    min: int
    average: float
    history: typing.List[typing.List[float]]


class TradesGetListItemsInfoResponse(BaseResponse):
    currency: Currency
    data: typing.Dict[str, TradesGetListItemsInfoData]
