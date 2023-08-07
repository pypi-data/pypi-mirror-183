from enum import Enum


class SkuOptionUpdateDataType(str, Enum):
    SKU_OPTIONS = "sku_options"

    def __str__(self) -> str:
        return str(self.value)
