from enum import Enum


class CustomerSubscriptionDataType(str, Enum):
    CUSTOMER_SUBSCRIPTIONS = "customer_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
