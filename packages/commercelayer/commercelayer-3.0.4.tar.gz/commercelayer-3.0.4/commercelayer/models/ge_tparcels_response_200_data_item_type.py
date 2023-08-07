from enum import Enum


class GETparcelsResponse200DataItemType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
