from enum import Enum


class PATCHparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcelDataType(str, Enum):
    PARCEL = "parcel"

    def __str__(self) -> str:
        return str(self.value)
