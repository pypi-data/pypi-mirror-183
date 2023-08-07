from enum import Enum


class GETordersorderIdResponse200DataRelationshipsShipmentsDataType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
