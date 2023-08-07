from enum import Enum


class POSTbingGeocodersResponse201DataRelationshipsAddressesDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
