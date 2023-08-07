from enum import Enum


class OrderSubscriptionCreateDataRelationshipsSourceOrderDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
