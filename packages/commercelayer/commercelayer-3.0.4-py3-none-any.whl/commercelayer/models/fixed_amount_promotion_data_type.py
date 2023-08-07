from enum import Enum


class FixedAmountPromotionDataType(str, Enum):
    FIXED_AMOUNT_PROMOTIONS = "fixed_amount_promotions"

    def __str__(self) -> str:
        return str(self.value)
