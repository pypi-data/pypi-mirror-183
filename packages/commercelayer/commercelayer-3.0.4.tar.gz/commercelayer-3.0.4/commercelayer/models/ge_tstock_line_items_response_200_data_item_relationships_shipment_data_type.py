from enum import Enum


class GETstockLineItemsResponse200DataItemRelationshipsShipmentDataType(str, Enum):
    SHIPMENT = "shipment"

    def __str__(self) -> str:
        return str(self.value)
