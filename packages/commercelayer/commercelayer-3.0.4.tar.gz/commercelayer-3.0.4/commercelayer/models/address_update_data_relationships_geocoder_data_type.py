from enum import Enum


class AddressUpdateDataRelationshipsGeocoderDataType(str, Enum):
    GEOCODERS = "geocoders"

    def __str__(self) -> str:
        return str(self.value)
