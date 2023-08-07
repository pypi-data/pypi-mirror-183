from enum import Enum


class POSTaddressesResponse201DataRelationshipsGeocoderDataType(str, Enum):
    GEOCODER = "geocoder"

    def __str__(self) -> str:
        return str(self.value)
