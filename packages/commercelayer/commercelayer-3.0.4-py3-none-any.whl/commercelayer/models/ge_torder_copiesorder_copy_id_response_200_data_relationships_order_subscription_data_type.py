from enum import Enum


class GETorderCopiesorderCopyIdResponse200DataRelationshipsOrderSubscriptionDataType(str, Enum):
    ORDER_SUBSCRIPTION = "order_subscription"

    def __str__(self) -> str:
        return str(self.value)
