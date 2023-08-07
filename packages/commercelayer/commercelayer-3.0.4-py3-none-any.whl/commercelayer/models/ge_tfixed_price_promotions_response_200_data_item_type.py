from enum import Enum


class GETfixedPricePromotionsResponse200DataItemType(str, Enum):
    FIXED_PRICE_PROMOTIONS = "fixed_price_promotions"

    def __str__(self) -> str:
        return str(self.value)
