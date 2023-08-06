import datetime
import typing

from market_api import models
from market_api.categories.base import BaseCategory

__all__ = (
    'TradesCategory',
)


class TradesCategory(BaseCategory):

    async def add_to_sale(
            self,
            item_id: int,
            price: int,
            currency: models.Currency
    ) -> models.TradesAddToSaleResponse:
        """Выставить предмет на продажу.

        Что-бы получить список предметов для выставления, воспользуйтесь методом `trades.my_inventory`.

        :param item_id:     id предмета в Steam, можно найти в описании вещей своего инвентаря в стиме.
        :param price:       сумма, целое число (1 USD=1000, 1 RUB=100, 1 EUR=1000)
        :param currency:    валюта. Дополнительная проверка,
                            если будет указана не равная текущей установленной в вашем аккаунте, покупка не произойдет.
                            Это защита от потери денег в случае, если вы сменили валюту на вашем аккаунте
                            и забыли про API
        :raise market_api.exceptions.MarketException:   bad_input — не верно указаны параметры<br>
                                                        inventory_not_loaded — необходимо обновить инвентарь<br>
                                                        item_not_recieved — необходимо обновить инвентарь<br>
                                                        no_description_found — стим не вернул описание предмета
                                                            попробуйте позже<br>
                                                        item_not_inserted — не удалось выставить на продажу<br>
                                                        item_not_in_inventory — Предмет не найден в инвентаре,
                                                            попробуйте сначала обновить его с помощью метода
                                                            UpdateInventory и подождать 10-20 секунд перед
                                                            повторной попыткой.<br>
                                                        bad_request — Неверно указана цена или вообще не указана
        """
        return models.TradesAddToSaleResponse.parse_obj(
            await self.client.request(
                'tadd-to-sale',
                id=item_id, price=price, currency=currency.value
            )
        )

    async def set_price(
            self,
            item_id: int,
            price: int,
            currency: models.Currency
    ) -> models.BaseResponse:
        """Установить новую цену на предмет, или снять с продажи.

        :param item_id:     ID предмета в нашей системе, его можно получить из результата запроса `add_to_sale`
        :param price:       сумма, целое число (1 USD=1000, 1 RUB=100, 1 EUR=1000),
                            **если указать 0 предмет будет снят с продажи**
        :param currency:    валюта `market_api.models.Currency` дополнительная проверка,
                            если будет указана не равная текущей установленной покупка не произойдет.
        :raise market_api.exceptions.MarketException: bad_item — предмет с данным ID не найден
        """
        return models.BaseResponse.parse_obj(
            await self.client.request(
                'set-price',
                item_id=item_id, price=price, currency=currency.value
            )
        )

    async def remove_all_from_sale(self) -> models.TradesRemoveAllFromSaleResponse:
        """Снятие сразу всех предметов с продажи.

        **ВАЖНО!**

        Предметы необходимо будет выставлять заново.
        Если Вы хотите остановить торговлю на время - используйте метод `account.go_offline`.
        """
        return models.TradesRemoveAllFromSaleResponse.parse_obj(
            await self.client.request(
                'remove-all-from-sale'
            )
        )

    async def my_inventory(self) -> models.TradesMyInventoryResponse:
        """Получение инвентаря Steam, только те предметы, которые Вы еще не выставили на продажу."""
        return models.TradesMyInventoryResponse.parse_obj(
            await self.client.request(
                'my-inventory'
            )
        )

    async def items(self) -> models.TradesItemsResponse:
        """Список предметов:

        * На продаже `status = ItemStatus.ADDED_TO_SALE`
        * Необходимых передать после продажи `status = ItemStatus.SALES`
        * Готовых к получению после покупки `status = ItemStatus.CAN_PICK_UP`
        """
        return models.TradesItemsResponse.parse_obj(
            await self.client.request(
                'items'
            )
        )

    async def ping(self) -> models.BaseResponse:
        """Включить продажи, необходимо отправлять раз в 3 минуты."""
        return models.BaseResponse.parse_obj(await self.client.request('ping'))

    async def trade_request_take(self, bot_id: typing.Optional[int] = None) -> models.TradesTradeRequestTakeResponse:
        """Создать запрос на передачу купленных предметов, находящихся на наших ботах.

        :param bot_id: id нашего бота у которого хотите забрать предметы, параметр не обязательный.
        :raise market_api.exceptions.MarketException: 3001 — нечего передавать.
        """
        return models.TradesTradeRequestTakeResponse.parse_obj(
            await self.client.request(
                'trade-request-take',
                botid=bot_id
            )
        )

    async def trade_request_give(self) -> models.TradesTradeRequestGiveResponse:
        """Создать запрос на передачу купленных предметов нашему боту"""
        return models.TradesTradeRequestGiveResponse.parse_obj(
            await self.client.request(
                'trade-request-give'
            )
        )

    async def trade_request_give_p2p(self) -> models.TradesTradeRequestGiveP2PResponse:
        """Запросить данные для передачи предмета покупателю (только для CS:GO, Dota2 и Rust)"""
        return models.TradesTradeRequestGiveP2PResponse.parse_obj(
            await self.client.request(
                'trade-request-give-p2p'
            )
        )

    async def trade_request_give_p2p_all(self) -> models.TradesTradeRequestGiveP2PAllResponse:
        """Запросить данные для передачи предмета покупателю (только для CS:GO, Dota2 и Rust)"""
        return models.TradesTradeRequestGiveP2PAllResponse.parse_obj(
            await self.client.request(
                'trade-request-give-p2p-all'
            )
        )

    async def trades(self, extended: typing.Optional[bool] = None) -> models.TradesTradesResponse:
        """Получить список трейд офферов, которые в данный момент были высланы Маркетом
        на Ваш аккаунт и ожидают подтверждения в Steam.

        :param extended: extended info
        """
        return models.TradesTradesResponse.parse_obj(
            await self.client.request('trades', extended=extended)
        )

    async def buy(
            self,
            price: int,
            custom_id: typing.Optional[str] = None,
            item_id: typing.Optional[int] = None,
            hash_name: typing.Optional[str] = None,
            partner: typing.Optional[int] = None,
            token: typing.Optional[str] = None
    ) -> models.TradesBuyResponse:
        """Покупка предмета. В нашей системе возможно покупка только по одному предмету за запрос.

        или

        Покупка предмета и передача его другому пользователю. Только для CS:GO, Dota2 и Rust

        :param price:       цена в копейках (1 RUB =100, 1 USD = 1000, 1 EUR = 1000) целое число, уже какого-то
                            выставленного лота, или можно указать любую сумму больше цены самого дешевого лота,
                            во втором случае будет куплен предмет по самой низкой цене.
        :param custom_id:   ваш уникальный ID (string[50]), по нему можно будет узнать статус операции
        :param item_id:     id предмета.
        :param hash_name:   `market_hash_name` идентификаторы предмета.
        :param partner:     параметры трейд ссылки аккаунта, который получит предмет.
        :param token:       параметры трейд ссылки аккаунта, который получит предмет.
        """
        return models.TradesBuyResponse.parse_obj(
            await self.client.request(
                'buy-for' if partner and token else 'buy',
                price=price, custom_id=custom_id,
                id=item_id, hash_name=hash_name,
                partner=partner, token=token
            )
        )

    async def get_buy_info_by_custom_id(
            self,
            custom_id: str
    ) -> models.TradesGetBuyInfoByCustomIDResponse:
        """Возвращает информацию о статусе покупки

        :param custom_id: Ваш уникальный ID заданный в методе `trades.buy`
        """
        return models.TradesGetBuyInfoByCustomIDResponse.parse_obj(
            await self.client.request(
                'get-buy-info-by-custom-id',
                custom_id=custom_id
            )
        )

    async def get_list_buy_info_by_custom_id(
            self,
            custom_ids: typing.List[str]
    ) -> models.TradesGetListBuyInfoByCustomIDResponse:
        """Возвращает информацию о статусе покупки

        :param custom_ids: Ваши уникальные ID заданные в методе `trades.buy`
        """
        return models.TradesGetListBuyInfoByCustomIDResponse.parse_obj(
            await self.client.request(
                'get-buy-info-by-custom-id',
                custom_id=custom_ids
            )
        )

    async def history(
            self,
            date: datetime.datetime,
            date_end: typing.Optional[datetime.datetime] = None
    ) -> models.TradesHistoryResponse:
        """История покупок и продаж на всех площадках"""
        return models.TradesHistoryResponse.parse_obj(
            await self.client.request(
                'history',
                date=date, date_end=date_end
            )
        )

    async def operation_history(
            self,
            date: datetime.datetime,
            date_end: datetime.datetime
    ) -> models.TradesOperationHistoryResponse:
        """История покупок, продаж, операций пополнений, выводов на всех площадках"""
        return models.TradesOperationHistoryResponse.parse_obj(
            await self.client.request(
                'operation-history',
                date=date, date_end=date_end
            )
        )

    async def test(self) -> models.TradesTestResponse:
        """Проверить все возможные препятствия к успешной продаже вещей."""
        return models.TradesTestResponse.parse_obj(
            await self.client.request(
                'test'
            )
        )

    async def get_list_items_info(self, list_hash_name: typing.List[str]) -> models.TradesGetListItemsInfoResponse:
        """Вариант для запроса по списку предметов"""
        return models.TradesGetListItemsInfoResponse.parse_obj(
            await self.client.request(
                'get-list-items-info',
                list_hash_name=list_hash_name
            )
        )
