from enum import Enum


class POSTlineItemsResponse201DataRelationshipsItemDataType(str, Enum):
    ITEM = "item"

    def __str__(self) -> str:
        return str(self.value)
