from enum import Enum


class PATCHparcelsparcelIdResponse200DataRelationshipsParcelLineItemsDataType(str, Enum):
    PARCEL_LINE_ITEMS = "parcel_line_items"

    def __str__(self) -> str:
        return str(self.value)
