from enum import Enum


class FreeGiftPromotionCreateDataRelationshipsSkuListPromotionRuleDataType(str, Enum):
    SKU_LIST_PROMOTION_RULES = "sku_list_promotion_rules"

    def __str__(self) -> str:
        return str(self.value)
