from enum import Enum


class ShippingMethodCreateDataRelationshipsShippingZoneDataType(str, Enum):
    SHIPPING_ZONES = "shipping_zones"

    def __str__(self) -> str:
        return str(self.value)
