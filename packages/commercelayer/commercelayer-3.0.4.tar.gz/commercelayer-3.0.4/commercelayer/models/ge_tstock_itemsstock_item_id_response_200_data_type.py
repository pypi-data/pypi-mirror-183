from enum import Enum


class GETstockItemsstockItemIdResponse200DataType(str, Enum):
    STOCK_ITEMS = "stock_items"

    def __str__(self) -> str:
        return str(self.value)
