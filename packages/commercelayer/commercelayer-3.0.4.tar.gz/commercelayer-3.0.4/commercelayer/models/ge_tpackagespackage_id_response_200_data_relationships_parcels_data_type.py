from enum import Enum


class GETpackagespackageIdResponse200DataRelationshipsParcelsDataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
