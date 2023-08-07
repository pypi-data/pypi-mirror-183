from enum import Enum


class POSTfreeShippingPromotionsResponse201DataType(str, Enum):
    FREE_SHIPPING_PROMOTIONS = "free_shipping_promotions"

    def __str__(self) -> str:
        return str(self.value)
