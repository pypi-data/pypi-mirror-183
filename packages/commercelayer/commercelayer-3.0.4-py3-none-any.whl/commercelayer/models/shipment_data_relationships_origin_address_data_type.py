from enum import Enum


class ShipmentDataRelationshipsOriginAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
