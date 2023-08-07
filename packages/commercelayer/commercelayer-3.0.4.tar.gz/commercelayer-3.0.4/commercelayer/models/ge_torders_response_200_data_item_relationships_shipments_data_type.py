from enum import Enum


class GETordersResponse200DataItemRelationshipsShipmentsDataType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
