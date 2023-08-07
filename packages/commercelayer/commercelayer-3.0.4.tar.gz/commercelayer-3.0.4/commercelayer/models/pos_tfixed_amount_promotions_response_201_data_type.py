from enum import Enum


class POSTfixedAmountPromotionsResponse201DataType(str, Enum):
    FIXED_AMOUNT_PROMOTIONS = "fixed_amount_promotions"

    def __str__(self) -> str:
        return str(self.value)
