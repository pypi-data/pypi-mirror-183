from enum import Enum


class GETorderSubscriptionsResponse200DataItemType(str, Enum):
    ORDER_SUBSCRIPTIONS = "order_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
