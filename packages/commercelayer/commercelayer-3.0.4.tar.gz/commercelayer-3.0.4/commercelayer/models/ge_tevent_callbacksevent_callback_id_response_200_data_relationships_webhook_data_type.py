from enum import Enum


class GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookDataType(str, Enum):
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
