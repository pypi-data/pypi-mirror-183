from enum import Enum


class PATCHparcelsparcelIdResponse200DataRelationshipsShipmentDataType(str, Enum):
    SHIPMENT = "shipment"

    def __str__(self) -> str:
        return str(self.value)
