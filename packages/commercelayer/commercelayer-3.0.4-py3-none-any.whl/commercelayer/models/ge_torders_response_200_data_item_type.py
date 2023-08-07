from enum import Enum


class GETordersResponse200DataItemType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
