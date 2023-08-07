from enum import Enum


class ParcelLineItemCreateDataRelationshipsParcelDataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
