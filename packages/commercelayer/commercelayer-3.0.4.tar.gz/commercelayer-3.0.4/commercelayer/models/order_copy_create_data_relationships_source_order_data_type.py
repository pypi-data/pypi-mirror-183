from enum import Enum


class OrderCopyCreateDataRelationshipsSourceOrderDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
