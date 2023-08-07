from enum import Enum


class GETlineItemsResponse200DataItemRelationshipsOrderDataType(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
