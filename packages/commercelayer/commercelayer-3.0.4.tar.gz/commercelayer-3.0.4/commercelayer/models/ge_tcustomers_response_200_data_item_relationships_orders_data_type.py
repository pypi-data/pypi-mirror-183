from enum import Enum


class GETcustomersResponse200DataItemRelationshipsOrdersDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
