from enum import Enum


class GETlineItemsResponse200DataItemRelationshipsItemDataType(str, Enum):
    ITEM = "item"

    def __str__(self) -> str:
        return str(self.value)
