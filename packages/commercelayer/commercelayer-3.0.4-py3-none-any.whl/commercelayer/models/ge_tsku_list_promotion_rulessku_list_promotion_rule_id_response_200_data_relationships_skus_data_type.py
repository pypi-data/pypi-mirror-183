from enum import Enum


class GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkusDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
