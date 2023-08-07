from enum import Enum


class StockTransferUpdateDataType(str, Enum):
    STOCK_TRANSFERS = "stock_transfers"

    def __str__(self) -> str:
        return str(self.value)
