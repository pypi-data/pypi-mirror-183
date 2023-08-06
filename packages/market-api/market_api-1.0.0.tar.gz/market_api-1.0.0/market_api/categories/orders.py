import typing

from market_api import models
from market_api.categories.base import BaseCategory

__all__ = (
    'OrdersCategory',
)


class OrdersCategory(BaseCategory):

    async def get(self, page: int = 0) -> models.OrdersGetResponse:
        """Получение списка ваших ордеров

        :param page: Параметр служит для постраничной выдачи. По умолчанию запрос возвращает последние 100 ордеров.
        """
        return models.OrdersGetResponse.parse_obj(
            await self.client.request(
                'get-orders',
                page=page
            )
        )

    async def set(
            self,
            market_hash_name: str,
            phase: models.OrderPhase,
            count: int,
            price: int,
            partner: typing.Optional[int] = None,
            token: typing.Optional[str] = None
    ) -> models.OrdersSetResponse:
        """Добавление, изменение и удаление ордера

        :param market_hash_name:  market_hash_name идентификаторы предмета.
        :param phase:             фаза предмета.
        :param count:             Количество покупаемых предметов
        :param price:             цена в копейках (1 RUB =100, 1 USD = 1000, 1 EUR = 1000) целое число
        :param partner:           Steam ID пользователя, кому будет передан купленный предмет
        :param token:             Токен из ссылки для обмена пользователя, которому будет передан предмет
        """
        return models.OrdersSetResponse.parse_obj(
            await self.client.request(
                'set-order',
                market_hash_name=market_hash_name,
                phase=phase, count=count, price=price,
                partner=partner, token=token
            )
        )

    async def get_log(self, page: int = 0) -> models.OrdersGetLogResponse:
        """История исполненных ордеров

        :param page: Параметр служит для постраничной выдачи. По умолчанию запрос возвращает последние 100 ордеров.
        """
        return models.OrdersGetLogResponse.parse_obj(
            await self.client.request(
                'get-orders-log',
                page=page
            )
        )
