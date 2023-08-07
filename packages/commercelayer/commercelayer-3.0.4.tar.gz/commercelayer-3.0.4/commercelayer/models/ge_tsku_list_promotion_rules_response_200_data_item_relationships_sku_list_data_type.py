from enum import Enum


class GETskuListPromotionRulesResponse200DataItemRelationshipsSkuListDataType(str, Enum):
    SKU_LIST = "sku_list"

    def __str__(self) -> str:
        return str(self.value)
