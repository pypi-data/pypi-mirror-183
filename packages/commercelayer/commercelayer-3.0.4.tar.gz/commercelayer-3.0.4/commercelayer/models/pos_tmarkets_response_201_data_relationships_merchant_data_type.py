from enum import Enum


class POSTmarketsResponse201DataRelationshipsMerchantDataType(str, Enum):
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
