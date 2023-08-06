import typing

from market_api import models
from market_api.categories.base import BaseCategory

__all__ = (
    'HistoryCategory',
)


class HistoryCategory(BaseCategory):

    async def checkout(self, page: int = 0) -> models.HistoryCheckoutResponse:
        """Получение истории операций выводов (100 на странице)

        :param page: Опциональный параметр. По умолчанию - 0. Страница в выдаче.
        """
        return models.HistoryCheckoutResponse.parse_obj(
            await self.client.request(
                'checkout-history',
                page=page
            )
        )

    async def checkin(self, page: int = 0) -> models.HistoryCheckoutResponse:
        """Получение истории операций пополнений (100 на странице)

        :param page: Опциональный параметр. По умолчанию - 0. Страница в выдаче.
        """
        return models.HistoryCheckoutResponse.parse_obj(
            await self.client.request(
                'checkin-history',
                page=page
            )
        )