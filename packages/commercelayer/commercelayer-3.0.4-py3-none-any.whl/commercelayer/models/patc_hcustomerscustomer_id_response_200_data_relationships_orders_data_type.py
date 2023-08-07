from enum import Enum


class PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
