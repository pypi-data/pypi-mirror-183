from enum import Enum


class GETstockTransfersstockTransferIdResponse200DataRelationshipsOriginStockLocationDataType(str, Enum):
    ORIGIN_STOCK_LOCATION = "origin_stock_location"

    def __str__(self) -> str:
        return str(self.value)
