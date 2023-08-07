from enum import Enum


class LineItemDataRelationshipsStockTransfersDataType(str, Enum):
    STOCK_TRANSFERS = "stock_transfers"

    def __str__(self) -> str:
        return str(self.value)
