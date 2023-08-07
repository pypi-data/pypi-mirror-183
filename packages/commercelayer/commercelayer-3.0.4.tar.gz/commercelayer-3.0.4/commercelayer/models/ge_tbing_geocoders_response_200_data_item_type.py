from enum import Enum


class GETbingGeocodersResponse200DataItemType(str, Enum):
    BING_GEOCODERS = "bing_geocoders"

    def __str__(self) -> str:
        return str(self.value)
