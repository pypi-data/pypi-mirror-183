import enum

import aenum

__all__ = (
    'Currency',
    'ItemStatus',
    'TradesTradesItemDirection',
    'BuyInfoStage',
    'Apps',
    'Event',
    'OperationHistoryStatus',
    'OrderPhase',
    'WSSChannel',
    'UnkItemStatus'
)


class Apps(aenum.MultiValueEnum):
    CS_GO = "730", 730
    DOTA_2 = "570", 570


class Currency(enum.Enum):
    """
    :var RUB: Рубли.
    :var USD: Доллары.
    :var EUR: Евро.
    """
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'


class ItemStatus(aenum.MultiValueEnum):
    """
    :var ADDED_TO_SALE: 1 — Вещь выставлена на продажу.
    :var SALES:         2 — Вы продали вещь и должны ее передать боту.
    :var WAIT:          3 — Ожидание передачи боту купленной вами вещи от продавца.
    :var CAN_PICK_UP:   4 — Вы можете забрать купленную вещь.
    """
    ADDED_TO_SALE = "1", 1
    SALES = "2", 2
    WAIT = "3", 3
    CAN_PICK_UP = "4", 4


class TradesTradesItemDirection(enum.Enum):
    """Направление трейда

    :var IN:    передача предмета который был продан
    :var OUT:   вывод предмета, который был куплен
    """
    IN = 'in'
    OUT = 'out'


class BuyInfoStage(aenum.MultiValueEnum):
    TRADE_STAGE_NEW = "1", 1
    TRADE_STAGE_ITEM_GIVEN = "2", 2
    TRADE_STAGE_TIMED_OUT = "5", 5


class Event(enum.Enum):
    SELL = 'sell'
    BUY = 'buy'
    CHECKOUT = 'checkout'


class OperationHistoryStatus(aenum.MultiValueEnum):
    """
    :var CREATED:             Заявка создана
    :var APPROVED:            Заявка одобрена
    :var SENT_FOR_EXECUTION:  Заявка отправлена на исполнение
    :var EXECUTED:            Заявка исполнена
    :var REJECTED:            Заявка отклонена
    :var CANCELED:            Заявка отменена
    :var ERROR:               Ошибка
    """
    CREATED = "0", 0
    APPROVED = "10", 10
    SENT_FOR_EXECUTION = "20", 20
    EXECUTED = "30", 30
    REJECTED = "100", 100
    CANCELED = "105", 105
    ERROR = "110", 110


class OrderPhase(enum.Enum):
    PHASE_1 = 'phase1'
    PHASE_2 = 'phase2'
    PHASE_3 = 'phase3'
    PHASE_4 = 'phase4'
    SAPPHIRE = 'sapphire'
    RUBY = 'ruby'
    BLACKPEARL = 'blackpearl'


# TODO: Узнать что это и зачем и относится ли это к BuyInfoStage
class UnkItemStatus(aenum.MultiValueEnum):
    ITEM_STATUS_IN_STORE = '1', 1
    ITEM_STATUS_MUST_BE_GET_OUT = '2', 2
    ITEM_STATUS_MUST_BE_GIVEN = '3', 3
    ITEM_STATUS_LOCKED_BY_BOT = '4', 4
    ITEM_STATUS_GIVEN = '5', 5
    ITEM_STATUS_CANCELLED = '6', 6
    ITEM_STATUS_WAITING_ACCEPT = '7', 7


class WSSChannel(enum.Enum):
    NEW_ITEMS_GO = 'newitems_go'
    HISTORY_GO = 'history_go'
    ADD_ITEM_GO = 'additem_go'
    ITEM_OUT_NEW_GO = 'itemout_new_go'
    ITEM_STATUS_GO = 'itemstatus_go'
    MONEY = 'money'
    WEB_NOTIFY = 'webnotify'
