import typing

from market_api import models
from market_api.categories.base import BaseCategory

__all__ = (
    'AccountCategory',
)


class AccountCategory(BaseCategory):

    async def get_money(self) -> models.AccountGetMoneyResponse:
        """Получить сумму на балансе и текущую валюту.

        **ВАЖНО!**

        Для валют USD и EUR установлена точность равная 1000, это значит,
        что торговля в этих валютах осуществляется с 3 (тремя) знаками после запятой.
        """
        return models.AccountGetMoneyResponse.parse_obj(
            await self.client.request(
                'get-money'
            )
        )

    async def go_offline(self) -> models.BaseResponse:
        """Моментально приостановить торги, рекомендуем также отключиться от вебсокетов."""
        return models.BaseResponse.parse_obj(
            await self.client.request(
                'go-offline'
            )
        )

    async def update_inventory(self) -> models.BaseResponse:
        """Запросить обновление кэша инвентаря (рекомендуется делать после каждого принятого трейд оффера)."""
        return models.BaseResponse.parse_obj(
            await self.client.request(
                'update-inventory'
            )
        )

    async def transfer_discounts(self, his_secret_key: str) -> models.BaseResponse:
        """Перенос скидок на другой аккаунт

        :param his_secret_key: API ключ аккаунта на который производится перенос скидок.
        """
        return models.BaseResponse.parse_obj(
            await self.client.request(
                'transfer-discounts', to=his_secret_key
            )
        )

    async def get_my_steam_id(self) -> models.AccountGetMySteamIDResponse:
        """Узнать свой steamID"""
        return models.AccountGetMySteamIDResponse.parse_obj(
            await self.client.request(
                'get-my-steam-id'
            )
        )

    async def set_pay_password(
            self,
            new_password: str,
            old_password: typing.Optional[str] = None
    ) -> models.BaseResponse:
        """Установка/смена платежного пароля.

        Возможна либо в первые 24 часа после регистрации, либо в любое время,
        но с указанным и подтвержденным почтовым адресом.

        :param old_password: Старый платежный пароль
                             (не указывается, если происходит первичная установка платежного пароля)
        :param new_password: Новый платежный пароль
        :return:
        """
        return models.BaseResponse.parse_obj(
            await self.client.request(
                'set-pay-password', old_password=old_password, new_password=new_password
            )
        )

    async def money_send(
            self,
            amount: int,
            user_api_key: str,
            pay_pass: str
    ) -> models.AccountMoneySendResponse:
        """Перенос баланса с текущего аккаунта на указанный

        **Возможен только при условии установленного платежного пароля**

        Минимальная сумма для переноса:
            * для рублей - 1000 руб.,
            * для долларов/евро - $10(€)

        Перенос с аккаунта на аккаунт с разными валютами производится по **курсу на текущий день**

        :param amount:        Целое число, сумма с копейками/центами, например<br>
                              100 руб. = 10000 (2 знака копеек),<br>
                              $10 (10€) = 10000 (3 знака у центов)
        :param user_api_key:  Апи ключ аккаунта на который будет производиться перенос баланса.
        :param pay_pass:      Текущий платежный пароль.

        """
        return models.AccountMoneySendResponse.parse_obj(
            await self.client.request(
                f'money-send/{amount}/{user_api_key}',
                pay_pass=pay_pass
            )
        )

    async def money_send_history(self, page: int = 0) -> models.AccountMoneySendHistoryResponse:
        """История переносов баланса с текущего аккаунта

        :param page: Опциональный параметр. По умолчанию - 0.
        """
        return models.AccountMoneySendHistoryResponse.parse_obj(
            await self.client.request(
                f'money-send-history/{page}'
            )
        )

    async def set_steam_api_key(self, steam_api_key: str) -> models.BaseResponse:
        """Привязка Steam API ключа к аккаунту

        :param steam_api_key: Ваш Steam API ключ.
        """
        return models.AccountMoneySendHistoryResponse.parse_obj(
            await self.client.request(
                f'set-steam-api-key',
                **{'steam-api-key': steam_api_key}
            )
        )

    async def set_trade_token(self, token: str) -> models.AccountSetTradeTokenResponse:
        """Привязка трейд-ссылки к аккаунту

        :param token: Ваш токен из трейд-ссылки
        """
        return models.AccountSetTradeTokenResponse.parse_obj(
            await self.client.request(
                f'set-trade-token', token=token
            )
        )

    async def change_currency(self, new_currency: models.Currency) -> models.BaseResponse:
        """Смена валюты аккаунта

        **ВАЖНО!**

         Смена валюты возможна для аккаунтов с нулевым балансом.
         Также не должно быть активных предметов для приема/передачи и активных заявок на вывод.

        :param new_currency: Новая валюта, которая будет установлена для аккаунта.
        :raise market_api.exceptions.MarketException:
            `1001` - Нельзя менять валюту, пока у Вас выставлены товары на продажу.
                Дождитесь когда их купят, или снимите с продажи.<br>
            `1003` - Нельзя менять валюту, пока у Вас есть активные заявки на вывод.
                Дождитесь когда они будут исполнены, или отмените их вручную.<br>
            `1004` - У Вас уже выбрана данная валюта<br>
            `1005` - Выбрана неверная валюта<br>
            `1007` - Ошибка.
                Вы два или более раз попытались отправить запрос на смену валюты.
                Если конвертация еще не завершилась, пожалуйста, подождите немного и обновите страницу.<br>
        """
        return models.AccountSetTradeTokenResponse.parse_obj(
            await self.client.request(
                f'change-currency/{new_currency.value}'
            )
        )
