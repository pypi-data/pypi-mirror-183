import typing

if typing.TYPE_CHECKING:
    from ..client import MarketClient


class BaseCategory:

    def __init__(self, client: "MarketClient"):
        self.client = client

