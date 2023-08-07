from enum import Enum


class GETorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsSourceOrderDataType(str, Enum):
    SOURCE_ORDER = "source_order"

    def __str__(self) -> str:
        return str(self.value)
