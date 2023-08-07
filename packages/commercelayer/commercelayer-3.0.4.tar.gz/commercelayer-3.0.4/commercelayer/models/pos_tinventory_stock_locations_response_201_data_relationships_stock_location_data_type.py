from enum import Enum


class POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationDataType(str, Enum):
    STOCK_LOCATION = "stock_location"

    def __str__(self) -> str:
        return str(self.value)
