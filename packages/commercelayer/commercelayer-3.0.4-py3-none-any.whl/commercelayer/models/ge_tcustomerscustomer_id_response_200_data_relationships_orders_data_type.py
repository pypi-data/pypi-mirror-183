from enum import Enum


class GETcustomerscustomerIdResponse200DataRelationshipsOrdersDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
