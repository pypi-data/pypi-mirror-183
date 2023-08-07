from enum import Enum


class ShippingMethodUpdateDataRelationshipsShippingMethodTiersDataType(str, Enum):
    SHIPPING_METHOD_TIERS = "shipping_method_tiers"

    def __str__(self) -> str:
        return str(self.value)
