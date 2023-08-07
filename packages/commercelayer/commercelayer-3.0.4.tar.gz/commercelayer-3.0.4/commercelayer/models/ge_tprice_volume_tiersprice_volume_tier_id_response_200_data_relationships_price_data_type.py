from enum import Enum


class GETpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPriceDataType(str, Enum):
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)
