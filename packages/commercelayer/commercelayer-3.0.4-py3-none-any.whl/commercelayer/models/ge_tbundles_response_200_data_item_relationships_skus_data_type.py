from enum import Enum


class GETbundlesResponse200DataItemRelationshipsSkusDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
