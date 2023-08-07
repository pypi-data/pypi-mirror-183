from enum import Enum


class PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPriceDataType(str, Enum):
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)
