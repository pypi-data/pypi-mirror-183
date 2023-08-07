from enum import Enum


class GETpricesResponse200DataItemRelationshipsPriceTiersDataType(str, Enum):
    PRICE_TIERS = "price_tiers"

    def __str__(self) -> str:
        return str(self.value)
