from enum import Enum


class OrderCreateDataRelationshipsShippingAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
