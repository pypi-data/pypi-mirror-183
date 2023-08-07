from enum import Enum


class EventDataRelationshipsWebhooksDataType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
