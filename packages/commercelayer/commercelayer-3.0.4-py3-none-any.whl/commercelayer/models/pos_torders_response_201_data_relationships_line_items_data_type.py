from enum import Enum


class POSTordersResponse201DataRelationshipsLineItemsDataType(str, Enum):
    LINE_ITEMS = "line_items"

    def __str__(self) -> str:
        return str(self.value)
