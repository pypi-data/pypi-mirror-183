from enum import Enum


class SkuUpdateDataRelationshipsShippingCategoryDataType(str, Enum):
    SHIPPING_CATEGORIES = "shipping_categories"

    def __str__(self) -> str:
        return str(self.value)
