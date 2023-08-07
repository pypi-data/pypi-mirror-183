from enum import Enum


class MarketCreateDataRelationshipsMerchantDataType(str, Enum):
    MERCHANTS = "merchants"

    def __str__(self) -> str:
        return str(self.value)
