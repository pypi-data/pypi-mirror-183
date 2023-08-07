from enum import Enum


class POSTpriceVolumeTiersResponse201DataRelationshipsPriceDataType(str, Enum):
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)
