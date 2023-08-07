from enum import Enum


class ShippingWeightTierUpdateDataRelationshipsShippingMethodDataType(str, Enum):
    SHIPPING_METHODS = "shipping_methods"

    def __str__(self) -> str:
        return str(self.value)
