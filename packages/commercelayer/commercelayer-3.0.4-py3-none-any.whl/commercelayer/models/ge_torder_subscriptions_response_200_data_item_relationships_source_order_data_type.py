from enum import Enum


class GETorderSubscriptionsResponse200DataItemRelationshipsSourceOrderDataType(str, Enum):
    SOURCE_ORDER = "source_order"

    def __str__(self) -> str:
        return str(self.value)
