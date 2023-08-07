from enum import Enum


class GETshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingMethodTiersDataType(str, Enum):
    SHIPPING_METHOD_TIERS = "shipping_method_tiers"

    def __str__(self) -> str:
        return str(self.value)
