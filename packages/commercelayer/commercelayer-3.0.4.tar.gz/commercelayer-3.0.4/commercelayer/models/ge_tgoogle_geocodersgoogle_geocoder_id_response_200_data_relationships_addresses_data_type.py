from enum import Enum


class GETgoogleGeocodersgoogleGeocoderIdResponse200DataRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
