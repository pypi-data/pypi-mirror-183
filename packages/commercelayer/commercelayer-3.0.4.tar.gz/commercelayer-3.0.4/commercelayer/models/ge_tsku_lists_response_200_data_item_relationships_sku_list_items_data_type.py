from enum import Enum


class GETskuListsResponse200DataItemRelationshipsSkuListItemsDataType(str, Enum):
    SKU_LIST_ITEMS = "sku_list_items"

    def __str__(self) -> str:
        return str(self.value)
