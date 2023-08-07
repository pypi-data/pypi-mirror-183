from enum import Enum


class ParcelLineItemDataRelationshipsShipmentLineItemDataType(str, Enum):
    SHIPMENT_LINE_ITEMS = "shipment_line_items"

    def __str__(self) -> str:
        return str(self.value)
