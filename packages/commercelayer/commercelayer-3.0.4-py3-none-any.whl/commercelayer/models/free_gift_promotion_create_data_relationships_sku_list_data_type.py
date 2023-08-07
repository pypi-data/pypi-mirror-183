from enum import Enum


class FreeGiftPromotionCreateDataRelationshipsSkuListDataType(str, Enum):
    SKU_LISTS = "sku_lists"

    def __str__(self) -> str:
        return str(self.value)
