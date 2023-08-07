from enum import Enum


class ShippingMethodUpdateDataRelationshipsStockLocationDataType(str, Enum):
    STOCK_LOCATIONS = "stock_locations"

    def __str__(self) -> str:
        return str(self.value)
