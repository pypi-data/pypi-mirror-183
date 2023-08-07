from enum import Enum


class GETshipmentsshipmentIdResponse200DataRelationshipsParcelsDataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
