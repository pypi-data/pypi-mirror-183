from enum import Enum


class GETordersResponse200DataItemRelationshipsOrderSubscriptionsDataType(str, Enum):
    ORDER_SUBSCRIPTIONS = "order_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
