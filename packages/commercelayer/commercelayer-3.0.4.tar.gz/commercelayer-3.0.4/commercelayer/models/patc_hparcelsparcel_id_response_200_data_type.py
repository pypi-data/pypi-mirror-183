from enum import Enum


class PATCHparcelsparcelIdResponse200DataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
