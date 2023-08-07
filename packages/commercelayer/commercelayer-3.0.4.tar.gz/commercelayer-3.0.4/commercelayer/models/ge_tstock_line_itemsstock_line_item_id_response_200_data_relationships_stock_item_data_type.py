from enum import Enum


class GETstockLineItemsstockLineItemIdResponse200DataRelationshipsStockItemDataType(str, Enum):
    STOCK_ITEM = "stock_item"

    def __str__(self) -> str:
        return str(self.value)
