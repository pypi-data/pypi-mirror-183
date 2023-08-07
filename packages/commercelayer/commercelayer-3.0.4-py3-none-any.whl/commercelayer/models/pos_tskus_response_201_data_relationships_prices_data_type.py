from enum import Enum


class POSTskusResponse201DataRelationshipsPricesDataType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
