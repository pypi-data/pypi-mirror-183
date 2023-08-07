from enum import Enum


class GETordersorderIdResponse200DataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
