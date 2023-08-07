from enum import Enum


class GETfixedAmountPromotionsResponse200DataItemType(str, Enum):
    FIXED_AMOUNT_PROMOTIONS = "fixed_amount_promotions"

    def __str__(self) -> str:
        return str(self.value)
