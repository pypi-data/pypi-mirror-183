from enum import Enum


class GETskuListItemsResponse200DataItemRelationshipsSkuListDataType(str, Enum):
    SKU_LIST = "sku_list"

    def __str__(self) -> str:
        return str(self.value)
