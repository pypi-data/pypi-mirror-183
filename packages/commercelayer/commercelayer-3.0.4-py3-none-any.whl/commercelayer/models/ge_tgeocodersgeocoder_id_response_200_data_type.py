from enum import Enum


class GETgeocodersgeocoderIdResponse200DataType(str, Enum):
    GEOCODERS = "geocoders"

    def __str__(self) -> str:
        return str(self.value)
