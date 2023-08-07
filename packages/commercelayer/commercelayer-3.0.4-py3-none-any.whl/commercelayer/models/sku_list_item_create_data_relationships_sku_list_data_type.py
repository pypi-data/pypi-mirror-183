from enum import Enum


class SkuListItemCreateDataRelationshipsSkuListDataType(str, Enum):
    SKU_LISTS = "sku_lists"

    def __str__(self) -> str:
        return str(self.value)
