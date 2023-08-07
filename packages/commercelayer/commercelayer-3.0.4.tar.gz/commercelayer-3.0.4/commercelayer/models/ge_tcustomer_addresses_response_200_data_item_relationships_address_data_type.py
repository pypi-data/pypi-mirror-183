from enum import Enum


class GETcustomerAddressesResponse200DataItemRelationshipsAddressDataType(str, Enum):
    ADDRESS = "address"

    def __str__(self) -> str:
        return str(self.value)
