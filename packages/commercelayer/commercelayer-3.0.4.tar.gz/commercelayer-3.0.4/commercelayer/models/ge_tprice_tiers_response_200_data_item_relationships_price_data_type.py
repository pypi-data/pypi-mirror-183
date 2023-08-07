from enum import Enum


class GETpriceTiersResponse200DataItemRelationshipsPriceDataType(str, Enum):
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)
