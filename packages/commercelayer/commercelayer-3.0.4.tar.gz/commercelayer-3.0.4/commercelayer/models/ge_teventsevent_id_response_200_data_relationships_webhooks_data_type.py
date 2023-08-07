from enum import Enum


class GETeventseventIdResponse200DataRelationshipsWebhooksDataType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
