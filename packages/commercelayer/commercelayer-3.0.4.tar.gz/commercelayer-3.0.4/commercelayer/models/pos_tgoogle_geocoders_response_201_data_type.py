from enum import Enum


class POSTgoogleGeocodersResponse201DataType(str, Enum):
    GOOGLE_GEOCODERS = "google_geocoders"

    def __str__(self) -> str:
        return str(self.value)
