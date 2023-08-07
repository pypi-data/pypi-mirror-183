from enum import Enum


class GETskuListsResponse200DataItemRelationshipsSkusDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
