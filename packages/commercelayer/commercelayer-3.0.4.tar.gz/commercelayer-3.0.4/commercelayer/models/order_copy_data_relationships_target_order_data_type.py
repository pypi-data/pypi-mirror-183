from enum import Enum


class OrderCopyDataRelationshipsTargetOrderDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
