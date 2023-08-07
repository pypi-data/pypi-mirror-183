from enum import Enum


class GETparcelsparcelIdResponse200DataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
