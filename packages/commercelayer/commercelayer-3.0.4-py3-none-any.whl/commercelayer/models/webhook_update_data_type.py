from enum import Enum


class WebhookUpdateDataType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
