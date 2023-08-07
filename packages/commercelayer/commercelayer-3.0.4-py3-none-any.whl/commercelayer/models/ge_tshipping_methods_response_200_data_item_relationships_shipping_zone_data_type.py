from enum import Enum


class GETshippingMethodsResponse200DataItemRelationshipsShippingZoneDataType(str, Enum):
    SHIPPING_ZONE = "shipping_zone"

    def __str__(self) -> str:
        return str(self.value)
