from enum import Enum


class POSTordersResponse201DataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
