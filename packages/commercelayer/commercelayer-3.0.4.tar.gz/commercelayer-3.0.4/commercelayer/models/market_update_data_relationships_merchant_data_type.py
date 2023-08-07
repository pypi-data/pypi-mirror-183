from enum import Enum


class MarketUpdateDataRelationshipsMerchantDataType(str, Enum):
    MERCHANTS = "merchants"

    def __str__(self) -> str:
        return str(self.value)
