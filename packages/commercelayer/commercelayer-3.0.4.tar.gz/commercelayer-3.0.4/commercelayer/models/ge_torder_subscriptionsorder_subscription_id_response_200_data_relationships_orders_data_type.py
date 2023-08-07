from enum import Enum


class GETorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrdersDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
