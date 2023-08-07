from enum import Enum


class POSTshippingZonesResponse201DataType(str, Enum):
    SHIPPING_ZONES = "shipping_zones"

    def __str__(self) -> str:
        return str(self.value)
