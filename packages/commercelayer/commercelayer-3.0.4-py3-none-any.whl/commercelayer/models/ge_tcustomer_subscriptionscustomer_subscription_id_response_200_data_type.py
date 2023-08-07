from enum import Enum


class GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataType(str, Enum):
    CUSTOMER_SUBSCRIPTIONS = "customer_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
