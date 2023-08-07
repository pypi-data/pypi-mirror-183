from enum import Enum


class GETlineItemOptionsResponse200DataItemRelationshipsSkuOptionDataType(str, Enum):
    SKU_OPTION = "sku_option"

    def __str__(self) -> str:
        return str(self.value)
