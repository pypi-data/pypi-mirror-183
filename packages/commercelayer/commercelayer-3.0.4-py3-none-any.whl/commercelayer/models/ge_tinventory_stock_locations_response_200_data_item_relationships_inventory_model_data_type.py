from enum import Enum


class GETinventoryStockLocationsResponse200DataItemRelationshipsInventoryModelDataType(str, Enum):
    INVENTORY_MODEL = "inventory_model"

    def __str__(self) -> str:
        return str(self.value)
