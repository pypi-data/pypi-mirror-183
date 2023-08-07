from enum import Enum


class PATCHskusskuIdResponse200DataRelationshipsShippingCategoryDataType(str, Enum):
    SHIPPING_CATEGORY = "shipping_category"

    def __str__(self) -> str:
        return str(self.value)
