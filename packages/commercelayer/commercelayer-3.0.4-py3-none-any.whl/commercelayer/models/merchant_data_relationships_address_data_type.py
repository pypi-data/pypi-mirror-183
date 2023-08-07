from enum import Enum


class MerchantDataRelationshipsAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
