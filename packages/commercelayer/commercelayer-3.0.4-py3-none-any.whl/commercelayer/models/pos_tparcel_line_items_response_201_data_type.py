from enum import Enum


class POSTparcelLineItemsResponse201DataType(str, Enum):
    PARCEL_LINE_ITEMS = "parcel_line_items"

    def __str__(self) -> str:
        return str(self.value)
