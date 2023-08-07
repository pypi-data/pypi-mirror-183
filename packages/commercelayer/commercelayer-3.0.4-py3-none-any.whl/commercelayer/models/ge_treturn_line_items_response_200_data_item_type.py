from enum import Enum


class GETreturnLineItemsResponse200DataItemType(str, Enum):
    RETURN_LINE_ITEMS = "return_line_items"

    def __str__(self) -> str:
        return str(self.value)
