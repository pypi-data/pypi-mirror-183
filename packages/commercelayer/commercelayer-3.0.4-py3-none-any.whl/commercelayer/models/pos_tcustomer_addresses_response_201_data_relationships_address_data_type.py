from enum import Enum


class POSTcustomerAddressesResponse201DataRelationshipsAddressDataType(str, Enum):
    ADDRESS = "address"

    def __str__(self) -> str:
        return str(self.value)
