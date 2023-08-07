from enum import Enum


class GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsDataType(str, Enum):
    INVENTORY_RETURN_LOCATIONS = "inventory_return_locations"

    def __str__(self) -> str:
        return str(self.value)
