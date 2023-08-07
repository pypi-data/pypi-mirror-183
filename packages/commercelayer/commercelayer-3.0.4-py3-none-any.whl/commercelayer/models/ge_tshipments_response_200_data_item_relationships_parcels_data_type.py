from enum import Enum


class GETshipmentsResponse200DataItemRelationshipsParcelsDataType(str, Enum):
    PARCELS = "parcels"

    def __str__(self) -> str:
        return str(self.value)
