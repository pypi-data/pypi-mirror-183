from enum import Enum


class GETpricesResponse200DataItemType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
