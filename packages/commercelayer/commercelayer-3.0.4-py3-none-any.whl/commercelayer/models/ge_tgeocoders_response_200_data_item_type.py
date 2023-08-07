from enum import Enum


class GETgeocodersResponse200DataItemType(str, Enum):
    GEOCODERS = "geocoders"

    def __str__(self) -> str:
        return str(self.value)
