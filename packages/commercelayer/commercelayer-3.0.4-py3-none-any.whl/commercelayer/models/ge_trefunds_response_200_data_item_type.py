from enum import Enum


class GETrefundsResponse200DataItemType(str, Enum):
    REFUNDS = "refunds"

    def __str__(self) -> str:
        return str(self.value)
