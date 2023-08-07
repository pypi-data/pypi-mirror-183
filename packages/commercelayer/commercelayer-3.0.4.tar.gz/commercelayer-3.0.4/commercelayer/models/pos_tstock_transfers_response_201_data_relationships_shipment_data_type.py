from enum import Enum


class POSTstockTransfersResponse201DataRelationshipsShipmentDataType(str, Enum):
    SHIPMENT = "shipment"

    def __str__(self) -> str:
        return str(self.value)
