from market_api import models
from market_api.categories.base import BaseCategory

__all__ = (
    'PricesCategory',
)


class PricesCategory(BaseCategory):

    async def get(self, currency: models.Currency = models.Currency.RUB) -> models.PricesResponse:
        """Список цен в формате json."""
        return models.PricesResponse.parse_obj(
            await self.client.request(
                f'prices/{currency.value}.json',
                need_auth=False
            )
        )

    async def get_class_instance(
            self,
            currency: models.Currency = models.Currency.RUB
    ) -> models.PricesClassInstanceResponse:
        """Список цен в формате json, где `buy_order` - максимальный **buy-ордер** на данный предмет."""
        return models.PricesClassInstanceResponse.parse_obj(
            await self.client.request(
                f'prices/class_instance/{currency.value}.json',
                need_auth=False
            )
        )