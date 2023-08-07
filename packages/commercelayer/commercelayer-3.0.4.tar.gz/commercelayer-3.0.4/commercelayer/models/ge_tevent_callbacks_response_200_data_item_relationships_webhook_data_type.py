from enum import Enum


class GETeventCallbacksResponse200DataItemRelationshipsWebhookDataType(str, Enum):
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
