from enum import Enum


class GETmarketsmarketIdResponse200DataRelationshipsMerchantDataType(str, Enum):
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
