from enum import Enum


class POSTlineItemOptionsResponse201DataRelationshipsSkuOptionDataType(str, Enum):
    SKU_OPTION = "sku_option"

    def __str__(self) -> str:
        return str(self.value)
