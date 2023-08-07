from enum import Enum


class LineItemOptionCreateDataRelationshipsLineItemDataType(str, Enum):
    LINE_ITEMS = "line_items"

    def __str__(self) -> str:
        return str(self.value)
