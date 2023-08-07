from enum import Enum


class CouponCodesPromotionRuleCreateDataRelationshipsCouponsDataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
