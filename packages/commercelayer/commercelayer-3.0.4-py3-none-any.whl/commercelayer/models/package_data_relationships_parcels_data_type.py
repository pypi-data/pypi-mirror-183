from enum import Enum


class PackageDataRelationshipsParcelsDataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
