from enum import Enum


class POSTordersResponse201DataRelationshipsShipmentsDataType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
