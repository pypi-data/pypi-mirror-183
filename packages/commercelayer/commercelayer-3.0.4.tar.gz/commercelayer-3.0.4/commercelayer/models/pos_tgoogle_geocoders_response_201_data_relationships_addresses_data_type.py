from enum import Enum


class POSTgoogleGeocodersResponse201DataRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
