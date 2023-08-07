from enum import Enum


class PATCHskusskuIdResponse200DataRelationshipsStockItemsDataType(str, Enum):
    STOCK_ITEMS = "stock_items"

    def __str__(self) -> str:
        return str(self.value)
