from enum import Enum


class POSTinventoryReturnLocationsResponse201DataRelationshipsInventoryModelDataType(str, Enum):
    INVENTORY_MODEL = "inventory_model"

    def __str__(self) -> str:
        return str(self.value)
