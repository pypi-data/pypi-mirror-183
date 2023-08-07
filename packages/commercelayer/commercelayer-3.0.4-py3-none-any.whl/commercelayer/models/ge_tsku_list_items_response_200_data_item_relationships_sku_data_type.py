from enum import Enum


class GETskuListItemsResponse200DataItemRelationshipsSkuDataType(str, Enum):
    SKU = "sku"

    def __str__(self) -> str:
        return str(self.value)
