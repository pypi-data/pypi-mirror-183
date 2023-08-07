from enum import Enum


class PATCHpricespriceIdResponse200DataType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
