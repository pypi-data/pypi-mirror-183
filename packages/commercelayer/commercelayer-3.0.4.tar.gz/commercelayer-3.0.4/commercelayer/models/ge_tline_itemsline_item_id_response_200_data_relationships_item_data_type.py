from enum import Enum


class GETlineItemslineItemIdResponse200DataRelationshipsItemDataType(str, Enum):
    ITEM = "item"

    def __str__(self) -> str:
        return str(self.value)
