from enum import Enum


class GETmarketsResponse200DataItemRelationshipsMerchantDataType(str, Enum):
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
