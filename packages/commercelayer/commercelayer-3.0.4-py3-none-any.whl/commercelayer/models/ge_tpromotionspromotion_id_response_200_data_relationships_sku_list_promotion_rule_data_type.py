from enum import Enum


class GETpromotionspromotionIdResponse200DataRelationshipsSkuListPromotionRuleDataType(str, Enum):
    SKU_LIST_PROMOTION_RULE = "sku_list_promotion_rule"

    def __str__(self) -> str:
        return str(self.value)
