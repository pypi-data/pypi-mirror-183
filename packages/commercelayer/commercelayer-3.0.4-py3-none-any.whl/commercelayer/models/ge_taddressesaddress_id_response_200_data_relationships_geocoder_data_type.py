from enum import Enum


class GETaddressesaddressIdResponse200DataRelationshipsGeocoderDataType(str, Enum):
    GEOCODER = "geocoder"

    def __str__(self) -> str:
        return str(self.value)
