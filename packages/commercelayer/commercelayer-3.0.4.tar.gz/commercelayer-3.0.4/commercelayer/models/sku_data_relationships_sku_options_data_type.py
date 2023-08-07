from enum import Enum


class SkuDataRelationshipsSkuOptionsDataType(str, Enum):
    SKU_OPTIONS = "sku_options"

    def __str__(self) -> str:
        return str(self.value)
