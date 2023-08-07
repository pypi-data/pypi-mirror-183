from enum import Enum


class PATCHbingGeocodersbingGeocoderIdResponse200DataType(str, Enum):
    BING_GEOCODERS = "bing_geocoders"

    def __str__(self) -> str:
        return str(self.value)
