from enum import Enum


class ParcelCreateDataRelationshipsShipmentDataType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
