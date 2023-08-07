from enum import Enum


class GETwebhooksResponse200DataItemType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
