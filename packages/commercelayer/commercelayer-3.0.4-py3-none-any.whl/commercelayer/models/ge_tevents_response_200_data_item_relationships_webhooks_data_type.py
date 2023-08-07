from enum import Enum


class GETeventsResponse200DataItemRelationshipsWebhooksDataType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
