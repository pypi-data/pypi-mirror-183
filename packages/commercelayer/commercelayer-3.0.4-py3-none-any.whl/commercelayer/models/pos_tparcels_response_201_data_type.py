from enum import Enum


class POSTparcelsResponse201DataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
