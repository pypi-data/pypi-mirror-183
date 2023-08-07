from enum import Enum


class GETstockLineItemsstockLineItemIdResponse200DataType(str, Enum):
    STOCK_LINE_ITEMS = "stock_line_items"

    def __str__(self) -> str:
        return str(self.value)
