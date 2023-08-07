from enum import Enum


class InventoryModelDataRelationshipsInventoryReturnLocationsDataType(str, Enum):
    INVENTORY_RETURN_LOCATIONS = "inventory_return_locations"

    def __str__(self) -> str:
        return str(self.value)
