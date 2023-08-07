from enum import Enum


class POSTorderSubscriptionsResponse201DataRelationshipsOrdersDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
