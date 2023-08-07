from enum import Enum


class GETshippingMethodsResponse200DataItemRelationshipsStockLocationDataType(str, Enum):
    STOCK_LOCATION = "stock_location"

    def __str__(self) -> str:
        return str(self.value)
