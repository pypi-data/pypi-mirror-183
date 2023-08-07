from enum import Enum


class GETpackagesResponse200DataItemRelationshipsParcelsDataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
