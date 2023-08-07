from enum import Enum


class MerchantUpdateDataRelationshipsAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
