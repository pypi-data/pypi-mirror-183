from enum import Enum


class PATCHgoogleGeocodersgoogleGeocoderIdResponse200DataRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
