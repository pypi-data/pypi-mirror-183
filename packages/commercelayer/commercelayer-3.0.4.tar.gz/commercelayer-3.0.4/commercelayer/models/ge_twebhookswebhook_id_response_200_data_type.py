from enum import Enum


class GETwebhookswebhookIdResponse200DataType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
