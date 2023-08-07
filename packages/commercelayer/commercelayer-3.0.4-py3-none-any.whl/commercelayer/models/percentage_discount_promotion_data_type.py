from enum import Enum


class PercentageDiscountPromotionDataType(str, Enum):
    PERCENTAGE_DISCOUNT_PROMOTIONS = "percentage_discount_promotions"

    def __str__(self) -> str:
        return str(self.value)
