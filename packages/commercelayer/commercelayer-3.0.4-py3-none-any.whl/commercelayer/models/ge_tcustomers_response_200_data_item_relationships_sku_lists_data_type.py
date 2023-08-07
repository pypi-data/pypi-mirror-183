from enum import Enum


class GETcustomersResponse200DataItemRelationshipsSkuListsDataType(str, Enum):
    SKU_LISTS = "sku_lists"

    def __str__(self) -> str:
        return str(self.value)
