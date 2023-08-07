from enum import Enum


class GETlineItemOptionsResponse200DataItemRelationshipsLineItemDataType(str, Enum):
    LINE_ITEM = "line_item"

    def __str__(self) -> str:
        return str(self.value)
