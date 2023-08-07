from enum import Enum


class GETstockTransfersstockTransferIdResponse200DataRelationshipsDestinationStockLocationDataType(str, Enum):
    DESTINATION_STOCK_LOCATION = "destination_stock_location"

    def __str__(self) -> str:
        return str(self.value)
