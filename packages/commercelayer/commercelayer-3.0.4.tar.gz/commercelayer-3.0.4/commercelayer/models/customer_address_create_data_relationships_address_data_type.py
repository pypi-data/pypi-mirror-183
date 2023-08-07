from enum import Enum


class CustomerAddressCreateDataRelationshipsAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
