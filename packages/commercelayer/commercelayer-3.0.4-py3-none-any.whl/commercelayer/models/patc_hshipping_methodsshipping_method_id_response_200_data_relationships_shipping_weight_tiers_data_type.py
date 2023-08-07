from enum import Enum


class PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingWeightTiersDataType(str, Enum):
    SHIPPING_WEIGHT_TIERS = "shipping_weight_tiers"

    def __str__(self) -> str:
        return str(self.value)
