from enum import Enum


class POSTparcelLineItemsResponse201DataRelationshipsParcelDataType(str, Enum):
    PARCEL = "parcel"

    def __str__(self) -> str:
        return str(self.value)
