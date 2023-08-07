from enum import Enum


class GETpriceListsResponse200DataItemType(str, Enum):
    PRICE_LISTS = "price_lists"

    def __str__(self) -> str:
        return str(self.value)
