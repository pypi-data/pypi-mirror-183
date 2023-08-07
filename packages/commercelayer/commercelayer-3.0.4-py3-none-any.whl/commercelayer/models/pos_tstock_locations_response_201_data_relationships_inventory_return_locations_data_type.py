from enum import Enum


class POSTstockLocationsResponse201DataRelationshipsInventoryReturnLocationsDataType(str, Enum):
    INVENTORY_RETURN_LOCATIONS = "inventory_return_locations"

    def __str__(self) -> str:
        return str(self.value)
