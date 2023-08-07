from enum import Enum


class POSTshippingCategoriesResponse201DataType(str, Enum):
    SHIPPING_CATEGORIES = "shipping_categories"

    def __str__(self) -> str:
        return str(self.value)
