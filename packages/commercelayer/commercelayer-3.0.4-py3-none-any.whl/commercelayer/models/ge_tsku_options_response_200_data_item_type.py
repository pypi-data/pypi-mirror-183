from enum import Enum


class GETskuOptionsResponse200DataItemType(str, Enum):
    SKU_OPTIONS = "sku_options"

    def __str__(self) -> str:
        return str(self.value)
