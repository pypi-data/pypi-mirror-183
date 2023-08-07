from enum import Enum


class GETinventoryStockLocationsResponse200DataItemRelationshipsStockLocationDataType(str, Enum):
    STOCK_LOCATION = "stock_location"

    def __str__(self) -> str:
        return str(self.value)
