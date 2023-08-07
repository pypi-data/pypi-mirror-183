from enum import Enum


class GETaddressesResponse200DataItemRelationshipsGeocoderDataType(str, Enum):
    GEOCODER = "geocoder"

    def __str__(self) -> str:
        return str(self.value)
