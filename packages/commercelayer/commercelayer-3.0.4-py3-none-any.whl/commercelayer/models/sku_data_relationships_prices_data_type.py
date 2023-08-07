from enum import Enum


class SkuDataRelationshipsPricesDataType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
