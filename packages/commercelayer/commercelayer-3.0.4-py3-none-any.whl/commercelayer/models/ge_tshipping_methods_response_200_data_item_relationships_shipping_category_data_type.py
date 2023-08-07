from enum import Enum


class GETshippingMethodsResponse200DataItemRelationshipsShippingCategoryDataType(str, Enum):
    SHIPPING_CATEGORY = "shipping_category"

    def __str__(self) -> str:
        return str(self.value)
