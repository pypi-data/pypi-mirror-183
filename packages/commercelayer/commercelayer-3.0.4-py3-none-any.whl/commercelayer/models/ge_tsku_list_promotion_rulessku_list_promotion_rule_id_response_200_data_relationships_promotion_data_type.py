from enum import Enum


class GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsPromotionDataType(str, Enum):
    PROMOTION = "promotion"

    def __str__(self) -> str:
        return str(self.value)
