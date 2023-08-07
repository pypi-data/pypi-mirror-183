from enum import Enum


class POSTfixedPricePromotionsResponse201DataType(str, Enum):
    FIXED_PRICE_PROMOTIONS = "fixed_price_promotions"

    def __str__(self) -> str:
        return str(self.value)
