from enum import Enum


class PATCHcustomerscustomerIdResponse200DataRelationshipsOrderSubscriptionsDataType(str, Enum):
    ORDER_SUBSCRIPTIONS = "order_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
