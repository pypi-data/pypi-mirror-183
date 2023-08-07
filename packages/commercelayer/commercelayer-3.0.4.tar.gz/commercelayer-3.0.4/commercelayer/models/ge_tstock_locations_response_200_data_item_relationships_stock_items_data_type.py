from enum import Enum


class GETstockLocationsResponse200DataItemRelationshipsStockItemsDataType(str, Enum):
    STOCK_ITEMS = "stock_items"

    def __str__(self) -> str:
        return str(self.value)
