from enum import Enum


class GETshippingCategoriesResponse200DataItemType(str, Enum):
    SHIPPING_CATEGORIES = "shipping_categories"

    def __str__(self) -> str:
        return str(self.value)
