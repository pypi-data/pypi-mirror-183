from enum import Enum


class PATCHinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryStockLocationsDataType(str, Enum):
    INVENTORY_STOCK_LOCATIONS = "inventory_stock_locations"

    def __str__(self) -> str:
        return str(self.value)
