import typing

from market_api import models
from market_api.categories.base import BaseCategory

__all__ = (
    'ItemsCategory',
)


class ItemsCategory(BaseCategory):

    async def search_by_hash_name(
            self,
            market_hash_name: str
    ) -> models.ItemsSearchByHashNameResponse:
        """Вариант для запроса по одному предмету

        :param market_hash_name: Название предмета, которое можно взять из инвентаря Steam.
        """
        return models.ItemsSearchByHashNameResponse.parse_obj(
            await self.client.request(
                'search-item-by-hash-name',
                hash_name=market_hash_name
            )
        )

    async def search_by_hash_name_specific(
            self,
            market_hash_name: str
    ) -> models.ItemsSearchByHashNameSpecificResponse:
        """Вариант для запроса по одному предмету

        :param market_hash_name: Название предмета, которое можно взять из инвентаря Steam.
        """
        return models.ItemsSearchByHashNameSpecificResponse.parse_obj(
            await self.client.request(
                'search-item-by-hash-name-specific',
                hash_name=market_hash_name
            )
        )

    async def search_list_by_hash_nane_all(
            self,
            list_hash_name: typing.List[str],
            extended: typing.Optional[bool] = None
    ) -> models.ItemsSearchListByHashNameAllResponse:
        """Вариант для запроса по списку предметов.
        Отдаёт **ограниченное** число предложений по списку market_hash_name.

        Если в url указан параметр `extended=True`, то максимальный лимит количества `market_hash_name` равен 5.
        По каждому предмету Вы получите 500 первых позиций на продажу.

        Если параметр `extended=True` НЕ указан, то максимальный лимит количества `market_hash_name` равен 50,
        при этом по каждому предмету Вы получите 50 первых позиций на продажу.

        :param list_hash_name: Название предмета, которое можно взять из инвентаря Steam.
        :param extended: ...
        """
        return models.ItemsSearchListByHashNameAllResponse.parse_obj(
            await self.client.request(
                'search-list-items-by-hash-name-all',
                list_hash_name=list_hash_name, extended=extended
            )
        )
