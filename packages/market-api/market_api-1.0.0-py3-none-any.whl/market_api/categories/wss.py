import logging
import typing

import aiohttp
import orjson
import pydantic

from market_api import models
from market_api.categories.base import BaseCategory

__all__ = (
    'WSSCategory',
)

logger = logging.getLogger('market_api.wss')


class WSSCategory(BaseCategory):
    """
    На нашей площадке присутствует возможность получать уведомления, изменения баланса,
    новые предметы на продаже и прочее.

    С помощью них можно только получать информацию, они работают по модели подписки.
    Для получения персональных оповещений достаточно отправить ключ-токен полученный методом get-ws-auth

   **ВАЖНО!**

    Ключ действует ограничено время и через 60 секунд перестает приниматься сервером.
    При ошибке авторизации на сервере уведомлений сервер пришлет строку: «auth»


    **Этапы подключения:**

    1. Устанавливается соединение с указанным на сайте сервером.

    2. Если Вы хотите получать информацию связанную с Вашим аккаунтом, посылаем на наш сервер ключ,
        который можно взять методом GetWSAuth.

    3. Если хотим просто ТОЛЬКО историю сделок или, например, список новых предметов - необходимо отправить название
        канала, на которых мы хотим подписаться: отправив `newitems_go` мы подпишемся на
        новые предложения по маркету CS:GO. `history_go` - подпишемся на получение
        информации о новых сделках на площадке

    4. Если мы подписались на персональные оповещения используя свой ключ - больше ничего делать не надо,
        просто слушаем входящие пакеты от нашего сервера и раз в 40-50 секунд отправляем «ping» на наш сервер.
        Все персональные уведомления (баланс, уведомления и прочее) будут приходить автоматический.


    **Доступные каналы:**

    * `newitems_go` - информация об изменениях в цене или выставлении на продажу предметов CS:GO. Осторожно, канал генерирует очень много трафика
    * `history_go` - история продаж которая отображается на каждой странице сайта.


    **Внимание!**

    Для нахождения в онлайне и продажи вещей необходимо отправлять команду ping раз минуту предварительно
    единожды отправив запрос к API методом PingPong.


    **Каналы не требующие подписки (при условии авторизации):**

    * `additem_go` - добавление предмета на странице "Мои вещи".
    * `itemout_new_go` - Исчезание предмета на странице "Мои вещи".
    * `itemstatus_go` - Изменение статуса предмета на странице "Мои вещи".
    * `money` - Изменение баланса пользователя.
    * `webnotify` - Получение уведомлений от администрации, доступности предмета для вывода, о покупках вещей.
    """

    async def get_auth(self) -> models.WSSGetAuthResponse:
        """Для получения персональных оповещений достаточно отправить ключ-токен полученный методом get-ws-auth

        **ВАЖНО!**

        Ключ действует ограничено время и через 60 секунд перестает приниматься сервером.
        При ошибке авторизации на сервере уведомлений сервер пришлет строку: «auth»
        """
        response = models.WSSGetAuthResponse.parse_obj(
            await self.client.request(
                'get-ws-auth'
            )
        )
        self.client.cfg.wss_key = response.wss_key
        return response

    async def _validate_message(self, message: aiohttp.WSMessage) -> models.WSSMessageTyping:
        try:
            data = orjson.loads(message.data)
            message_type = data['type']
            message_data = orjson.loads(data['data'])
        except:
            if message.data == 'auth':
                await self.get_auth()
            return message.data
        try:
            if message_type == models.WSSChannel.NEW_ITEMS_GO.value:
                return models.WSSMessageNewItemsGo.parse_obj(dict(type=message_type, data=message_data))
            if message_type == models.WSSChannel.HISTORY_GO.value:
                message_data = orjson.loads(message_data)
                return models.WSSMessageHistoryGo.from_message(message_data)
            if message_type == models.WSSChannel.ADD_ITEM_GO.value:
                return models.WSSMessageAddItemGo.parse_obj(dict(type=message_type, data=message_data))
            if message_type == models.WSSChannel.ITEM_STATUS_GO.value:
                return models.WSSMessageItemStatusGo.parse_obj(dict(type=message_type, data=message_data))
            if message_type == models.WSSChannel.ITEM_OUT_NEW_GO.value:
                return models.WSSMessageItemOutNewGo.parse_obj(dict(type=message_type, data=message_data))
            if message_type == models.WSSChannel.WEB_NOTIFY.value:
                return models.WSSMessageWebNotify.parse_obj(dict(type=message_type, data=message_data))
        except pydantic.ValidationError:
            pass
        return {
            'type': models.WSSChannel(message_type),
            'data': message_data
        }

    async def listen_raw(
            self,
            channels: typing.List[models.WSSChannel] = None,
            need_auth: bool = True
    ) -> typing.AsyncGenerator[aiohttp.WSMessage]:
        if channels is None:
            channels = []
        if need_auth and not self.client.cfg.wss_key:
            await self.get_auth()

        async with self.client.session.ws_connect(self.client.cfg.wss_url) as ws:
            if need_auth:
                logger.debug("Send to ws: key")
                await ws.send_str(self.client.cfg.wss_key)
            for channel in channels:
                logger.debug(f"Send to ws: {channel.value}")
                await ws.send_str(channel.value)
            async for message in ws:
                logger.debug(f"New message from ws: {message}")
                yield message

    async def listen(
            self,
            channels: typing.List[models.WSSChannel] = None,
            need_auth: bool = True
    ) -> typing.AsyncGenerator[models.WSSMessageTyping]:
        """У маркета не понятно что творится с тайпингами поэтому лучше использовать пока что
        `listen_raw` и творить грязь с ним
        """
        async for message in self.listen_raw(channels, need_auth):
            yield await self._validate_message(message)
