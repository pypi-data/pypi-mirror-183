from enum import Enum


class GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcelDataType(str, Enum):
    PARCEL = "parcel"

    def __str__(self) -> str:
        return str(self.value)
