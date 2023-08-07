from enum import Enum


class PATCHstockTransfersstockTransferIdResponse200DataType(str, Enum):
    STOCK_TRANSFERS = "stock_transfers"

    def __str__(self) -> str:
        return str(self.value)
