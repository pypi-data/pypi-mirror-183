from enum import Enum


class GETcustomersResponse200DataItemRelationshipsReturnsDataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
