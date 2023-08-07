from enum import Enum


class POSTorderSubscriptionsResponse201DataRelationshipsOrderCopiesDataType(str, Enum):
    ORDER_COPIES = "order_copies"

    def __str__(self) -> str:
        return str(self.value)
