from enum import Enum


class PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrdersDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
