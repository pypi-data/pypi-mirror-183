from enum import Enum


class GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
