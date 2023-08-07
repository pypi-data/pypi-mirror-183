from enum import Enum


class PATCHaddressesaddressIdResponse200DataRelationshipsGeocoderDataType(str, Enum):
    GEOCODER = "geocoder"

    def __str__(self) -> str:
        return str(self.value)
