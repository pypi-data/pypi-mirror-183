from enum import Enum


class GETshippingMethodsResponse200DataItemType(str, Enum):
    SHIPPING_METHODS = "shipping_methods"

    def __str__(self) -> str:
        return str(self.value)
