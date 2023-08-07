from enum import Enum


class GETpriceListsResponse200DataItemRelationshipsPricesDataType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
