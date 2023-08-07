from enum import Enum


class GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemDataType(str, Enum):
    SHIPMENT_LINE_ITEM = "shipment_line_item"

    def __str__(self) -> str:
        return str(self.value)
