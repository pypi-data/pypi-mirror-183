from enum import Enum


class GETcouponCodesPromotionRulescouponCodesPromotionRuleIdResponse200DataRelationshipsPromotionDataType(str, Enum):
    PROMOTION = "promotion"

    def __str__(self) -> str:
        return str(self.value)
