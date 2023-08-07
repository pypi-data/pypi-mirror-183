from enum import Enum


class PriceVolumeTierUpdateDataRelationshipsPriceDataType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
