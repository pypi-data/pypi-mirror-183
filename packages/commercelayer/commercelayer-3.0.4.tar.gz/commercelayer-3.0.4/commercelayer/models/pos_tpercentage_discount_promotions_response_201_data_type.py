from enum import Enum


class POSTpercentageDiscountPromotionsResponse201DataType(str, Enum):
    PERCENTAGE_DISCOUNT_PROMOTIONS = "percentage_discount_promotions"

    def __str__(self) -> str:
        return str(self.value)
