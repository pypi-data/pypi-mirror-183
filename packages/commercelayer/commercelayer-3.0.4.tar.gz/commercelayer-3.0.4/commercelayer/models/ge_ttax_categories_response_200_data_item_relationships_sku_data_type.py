from enum import Enum


class GETtaxCategoriesResponse200DataItemRelationshipsSkuDataType(str, Enum):
    SKU = "sku"

    def __str__(self) -> str:
        return str(self.value)
