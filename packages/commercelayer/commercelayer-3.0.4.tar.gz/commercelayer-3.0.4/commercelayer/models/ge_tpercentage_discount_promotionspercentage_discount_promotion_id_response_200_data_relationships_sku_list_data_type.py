from enum import Enum


class GETpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsSkuListDataType(
    str, Enum
):
    SKU_LIST = "sku_list"

    def __str__(self) -> str:
        return str(self.value)
