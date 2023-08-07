from enum import Enum


class AddressDataRelationshipsGeocoderDataType(str, Enum):
    GEOCODERS = "geocoders"

    def __str__(self) -> str:
        return str(self.value)
