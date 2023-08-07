from enum import Enum


class PATCHpriceListspriceListIdResponse200DataRelationshipsPricesDataType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
