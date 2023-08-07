from enum import Enum


class StockLocationCreateDataRelationshipsAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
