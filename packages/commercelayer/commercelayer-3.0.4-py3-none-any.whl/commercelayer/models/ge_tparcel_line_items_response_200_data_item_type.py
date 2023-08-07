from enum import Enum


class GETparcelLineItemsResponse200DataItemType(str, Enum):
    PARCEL_LINE_ITEMS = "parcel_line_items"

    def __str__(self) -> str:
        return str(self.value)
