from enum import Enum


class GETbingGeocodersbingGeocoderIdResponse200DataRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
