from enum import Enum


class GETparcelLineItemsResponse200DataItemRelationshipsParcelDataType(str, Enum):
    PARCEL = "parcel"

    def __str__(self) -> str:
        return str(self.value)
