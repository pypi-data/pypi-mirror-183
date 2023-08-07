from enum import Enum


class POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionDataType(str, Enum):
    ORDER_SUBSCRIPTION = "order_subscription"

    def __str__(self) -> str:
        return str(self.value)
