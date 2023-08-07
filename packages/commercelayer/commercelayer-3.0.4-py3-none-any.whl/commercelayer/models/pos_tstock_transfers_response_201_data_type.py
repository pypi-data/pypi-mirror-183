from enum import Enum


class POSTstockTransfersResponse201DataType(str, Enum):
    STOCK_TRANSFERS = "stock_transfers"

    def __str__(self) -> str:
        return str(self.value)
