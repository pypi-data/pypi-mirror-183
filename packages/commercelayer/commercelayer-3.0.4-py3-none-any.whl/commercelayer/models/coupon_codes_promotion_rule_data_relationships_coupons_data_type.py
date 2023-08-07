from enum import Enum


class CouponCodesPromotionRuleDataRelationshipsCouponsDataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
