from enum import Enum


class PATCHstockLocationsstockLocationIdResponse200DataRelationshipsStockItemsDataType(str, Enum):
    STOCK_ITEMS = "stock_items"

    def __str__(self) -> str:
        return str(self.value)
