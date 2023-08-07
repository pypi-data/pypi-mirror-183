from enum import Enum


class FreeGiftPromotionUpdateDataRelationshipsCouponCodesPromotionRuleDataType(str, Enum):
    COUPON_CODES_PROMOTION_RULES = "coupon_codes_promotion_rules"

    def __str__(self) -> str:
        return str(self.value)
