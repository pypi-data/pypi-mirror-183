from enum import Enum


class GETparcelLineItemsResponse200DataItemRelationshipsShipmentLineItemDataType(str, Enum):
    SHIPMENT_LINE_ITEM = "shipment_line_item"

    def __str__(self) -> str:
        return str(self.value)
