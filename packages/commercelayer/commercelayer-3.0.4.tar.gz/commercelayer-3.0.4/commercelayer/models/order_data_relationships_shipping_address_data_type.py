from enum import Enum


class OrderDataRelationshipsShippingAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
