from enum import Enum


class OrderSubscriptionDataRelationshipsOrderCopiesDataType(str, Enum):
    ORDER_COPIES = "order_copies"

    def __str__(self) -> str:
        return str(self.value)
