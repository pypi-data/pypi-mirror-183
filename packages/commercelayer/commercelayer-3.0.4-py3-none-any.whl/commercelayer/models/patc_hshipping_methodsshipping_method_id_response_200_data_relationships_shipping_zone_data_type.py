from enum import Enum


class PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingZoneDataType(str, Enum):
    SHIPPING_ZONE = "shipping_zone"

    def __str__(self) -> str:
        return str(self.value)
