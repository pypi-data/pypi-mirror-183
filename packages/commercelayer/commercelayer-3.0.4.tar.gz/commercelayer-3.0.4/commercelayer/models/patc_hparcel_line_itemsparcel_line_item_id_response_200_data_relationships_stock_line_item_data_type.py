from enum import Enum


class PATCHparcelLineItemsparcelLineItemIdResponse200DataRelationshipsStockLineItemDataType(str, Enum):
    STOCK_LINE_ITEM = "stock_line_item"

    def __str__(self) -> str:
        return str(self.value)
