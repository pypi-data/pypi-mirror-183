from enum import Enum


class GETgoogleGeocodersResponse200DataItemRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
