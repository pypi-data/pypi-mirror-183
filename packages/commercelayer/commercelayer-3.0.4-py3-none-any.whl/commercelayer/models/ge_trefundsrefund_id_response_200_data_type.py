from enum import Enum


class GETrefundsrefundIdResponse200DataType(str, Enum):
    REFUNDS = "refunds"

    def __str__(self) -> str:
        return str(self.value)
