from enum import Enum


class StockTransferDataRelationshipsLineItemDataType(str, Enum):
    LINE_ITEMS = "line_items"

    def __str__(self) -> str:
        return str(self.value)
