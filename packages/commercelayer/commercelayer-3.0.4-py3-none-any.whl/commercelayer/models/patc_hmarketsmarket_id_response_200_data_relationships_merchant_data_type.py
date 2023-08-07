from enum import Enum


class PATCHmarketsmarketIdResponse200DataRelationshipsMerchantDataType(str, Enum):
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
