from enum import Enum


class PATCHshippingWeightTiersshippingWeightTierIdResponse200DataType(str, Enum):
    SHIPPING_WEIGHT_TIERS = "shipping_weight_tiers"

    def __str__(self) -> str:
        return str(self.value)
