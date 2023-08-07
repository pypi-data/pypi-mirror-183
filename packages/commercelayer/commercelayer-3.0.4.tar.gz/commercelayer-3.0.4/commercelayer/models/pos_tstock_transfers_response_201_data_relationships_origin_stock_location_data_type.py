from enum import Enum


class POSTstockTransfersResponse201DataRelationshipsOriginStockLocationDataType(str, Enum):
    ORIGIN_STOCK_LOCATION = "origin_stock_location"

    def __str__(self) -> str:
        return str(self.value)
