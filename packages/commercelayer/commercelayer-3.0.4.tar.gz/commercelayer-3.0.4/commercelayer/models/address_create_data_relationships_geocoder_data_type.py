from enum import Enum


class AddressCreateDataRelationshipsGeocoderDataType(str, Enum):
    GEOCODERS = "geocoders"

    def __str__(self) -> str:
        return str(self.value)
