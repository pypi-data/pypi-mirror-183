from enum import Enum


class ShippingMethodDataRelationshipsStockLocationDataType(str, Enum):
    STOCK_LOCATIONS = "stock_locations"

    def __str__(self) -> str:
        return str(self.value)
