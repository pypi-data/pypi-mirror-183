from enum import Enum


class PATCHordersorderIdResponse200DataRelationshipsShipmentsDataType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
