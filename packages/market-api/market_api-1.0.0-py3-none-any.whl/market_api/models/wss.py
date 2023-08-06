import datetime
import typing

import pydantic

from market_api.models import BaseResponse
from market_api.models.enum import *


class WSSGetAuthResponse(BaseResponse):
    wss_key: str = pydantic.Field(alias='wsAuth')


class WSSMessage(pydantic.BaseModel):
    type: WSSChannel


class WSSMessageNewItemsGoData(pydantic.BaseModel):
    quality: typing.Optional[str] = pydantic.Field(alias='i_quality')
    name_color: typing.Optional[str] = pydantic.Field(alias='i_name_color')
    class_id: int = pydantic.Field(alias='i_classid')
    instance_id: int = pydantic.Field(alias='i_instanceid')
    market_hash_name: str = pydantic.Field(alias='i_market_hash_name')
    market_name: str = pydantic.Field(alias='i_market_name')
    price: float = pydantic.Field(alias='ui_price')
    currency: Currency = pydantic.Field(alias='ui_currency')
    id: int = pydantic.Field(alias='ui_id')
    app: str


class WSSMessageNewItemsGo(WSSMessage):
    data: WSSMessageNewItemsGoData


class WSSMessageHistoryGoData(pydantic.BaseModel):
    unk_1: int
    unk_2: int
    market_hash_name: str
    time: datetime.datetime
    price: int
    market_hash_name_ru: str
    color: str
    currency: Currency
    unk_4: int


class WSSMessageHistoryGo(WSSMessage):
    data: WSSMessageHistoryGoData

    @classmethod
    def from_message(cls, value: dict):
        # TODO: Узнать что же все таки тут передается
        return cls(
            type=WSSChannel.HISTORY_GO,
            data=WSSMessageHistoryGoData(
                unk_1=int(value[0]),
                unk_2=int(value[1]),
                market_hash_name=value[2],
                time=datetime.datetime.fromtimestamp(int(value[3])),
                price=int(value[4]),
                market_hash_name_ru=value[5],
                color=value[6],
                currency=Currency(value[7]),
                unk_4=int(value[8])
            )
        )


class WSSMessageAddItemGoData(pydantic.BaseModel):
    currency: Currency = pydantic.Field(alias="currency")
    he_name: str = pydantic.Field(alias="he_name")
    class_id: int = pydantic.Field(alias="i_classid")
    descriptions: typing.Any = pydantic.Field(alias="i_descriptions")
    instance_id: int = pydantic.Field(alias="i_instanceid")
    market_hash_name: str = pydantic.Field(alias="i_market_hash_name")
    market_name: str = pydantic.Field(alias="i_market_name")
    market_price: float = pydantic.Field(alias="i_market_price")
    market_price_text: str = pydantic.Field(alias="i_market_price_text")
    name: str = pydantic.Field(alias="i_name")
    name_color: str = pydantic.Field(alias="i_name_color")
    quality: str = pydantic.Field(alias="i_quality")
    rarity: str = pydantic.Field(alias="i_rarity")
    rarity_en: str = pydantic.Field(alias="i_rarity_en")
    min_price: float = pydantic.Field(alias="min_price")
    min_price_text: bool = pydantic.Field(alias="min_price_text")
    offer_live_time: int = pydantic.Field(alias="offer_live_time")
    placed: str = pydantic.Field(alias="placed")
    position: int = pydantic.Field(alias="position")
    roulette: int = pydantic.Field(alias="roulette")
    sc_id: typing.Any = pydantic.Field(alias="sc_id")
    type: int = pydantic.Field(alias="type")
    asset: int = pydantic.Field(alias="ui_asset")
    bid: int = pydantic.Field(alias="ui_bid")
    id: int = pydantic.Field(alias="ui_id")
    phase: str = pydantic.Field(alias="ui_phase")
    price: int = pydantic.Field(alias="ui_price")
    price_text: str = pydantic.Field(alias="ui_price_text")
    real_instance: int = pydantic.Field(alias="ui_real_instance")
    status: int = pydantic.Field(alias="ui_status")
    uid: int = pydantic.Field(alias="ui_uid")


class WSSMessageAddItemGo(WSSMessage):
    data: WSSMessageAddItemGoData


class WSSMessageItemStatusGoData(pydantic.BaseModel):
    id: int
    status: UnkItemStatus


class WSSMessageItemStatusGo(WSSMessage):
    data: WSSMessageItemStatusGoData


class WSSMessageItemOutNewGoData(pydantic.BaseModel):
    currency: Currency = pydantic.Field(alias="currency")
    he_name: str = pydantic.Field(alias="he_name")
    class_id: int = pydantic.Field(alias="i_classid")
    descriptions: typing.Any = pydantic.Field(alias="i_descriptions")
    instance_id: int = pydantic.Field(alias="i_instanceid")
    market_hash_name: str = pydantic.Field(alias="i_market_hash_name")
    market_name: str = pydantic.Field(alias="i_market_name")
    market_price: float = pydantic.Field(alias="i_market_price")
    market_price_text: str = pydantic.Field(alias="i_market_price_text")
    name: str = pydantic.Field(alias="i_name")
    name_color: str = pydantic.Field(alias="i_name_color")
    quality: str = pydantic.Field(alias="i_quality")
    rarity: str = pydantic.Field(alias="i_rarity")
    left: int = pydantic.Field(alias="left")
    min_price: int = pydantic.Field(alias="min_price")
    min_price_text: bool = pydantic.Field(alias="min_price_text")
    placed: str = pydantic.Field(alias="placed")
    position: int = pydantic.Field(alias="position")
    roulette: int = pydantic.Field(alias="roulette")
    send_until: int = pydantic.Field(alias="send_until")
    type: int = pydantic.Field(alias="type")
    asset: int = pydantic.Field(alias="ui_asset")
    bid: int = pydantic.Field(alias="ui_bid")
    id: int = pydantic.Field(alias="ui_id")
    price: float = pydantic.Field(alias="ui_price")
    price_text: str = pydantic.Field(alias="ui_price_text")
    real_instance: int = pydantic.Field(alias="ui_real_instance")
    status: int = pydantic.Field(alias="ui_status")
    warranty: int = pydantic.Field(alias="warranty")


class WSSMessageItemOutNewGo(WSSMessage):
    data: WSSMessageItemOutNewGoData


class WSSMessageWebNotifyData(pydantic.BaseModel):
    class_id: int = pydantic.Field(alias="class")
    instance_id: int = pydantic.Field(alias="i_instanceid")
    way: str
    app: str
    price: str
    name: str
    tag: int


class WSSMessageWebNotify(WSSMessage):
    data: WSSMessageWebNotifyData


WSSMessageTyping = typing.Union[
    WSSMessageNewItemsGo,
    WSSMessageHistoryGo,
    WSSMessageAddItemGo,
    WSSMessageItemStatusGo,
    WSSMessageItemOutNewGo,
    WSSMessageWebNotify,
    str,
    dict
]
