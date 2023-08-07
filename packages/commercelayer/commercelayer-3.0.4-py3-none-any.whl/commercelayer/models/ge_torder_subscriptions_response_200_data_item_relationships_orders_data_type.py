from enum import Enum


class GETorderSubscriptionsResponse200DataItemRelationshipsOrdersDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
