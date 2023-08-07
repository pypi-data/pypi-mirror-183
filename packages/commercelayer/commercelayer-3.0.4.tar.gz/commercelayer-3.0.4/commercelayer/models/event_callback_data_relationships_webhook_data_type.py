from enum import Enum


class EventCallbackDataRelationshipsWebhookDataType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
