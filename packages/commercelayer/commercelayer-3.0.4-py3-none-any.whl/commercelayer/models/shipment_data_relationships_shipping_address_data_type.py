from enum import Enum


class ShipmentDataRelationshipsShippingAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
