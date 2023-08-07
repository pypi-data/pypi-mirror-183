from enum import Enum


class GETshippingCategoriesshippingCategoryIdResponse200DataType(str, Enum):
    SHIPPING_CATEGORIES = "shipping_categories"

    def __str__(self) -> str:
        return str(self.value)
