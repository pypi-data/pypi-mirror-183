from enum import Enum


class GETpriceVolumeTiersResponse200DataItemRelationshipsPriceDataType(str, Enum):
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)
