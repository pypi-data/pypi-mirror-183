from enum import Enum


class PATCHgoogleGeocodersgoogleGeocoderIdResponse200DataType(str, Enum):
    GOOGLE_GEOCODERS = "google_geocoders"

    def __str__(self) -> str:
        return str(self.value)
