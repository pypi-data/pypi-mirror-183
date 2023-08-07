from enum import Enum


class ParcelLineItemDataRelationshipsParcelDataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
