from enum import Enum


class GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsInventoryModelDataType(str, Enum):
    INVENTORY_MODEL = "inventory_model"

    def __str__(self) -> str:
        return str(self.value)
