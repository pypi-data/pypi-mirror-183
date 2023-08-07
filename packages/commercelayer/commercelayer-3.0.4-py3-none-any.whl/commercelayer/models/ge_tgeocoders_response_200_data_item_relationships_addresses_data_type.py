from enum import Enum


class GETgeocodersResponse200DataItemRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
