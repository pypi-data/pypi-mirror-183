from enum import Enum


class PriceDataRelationshipsPriceTiersDataType(str, Enum):
    PRICE_TIERS = "price_tiers"

    def __str__(self) -> str:
        return str(self.value)
