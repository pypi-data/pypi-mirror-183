from enum import Enum


class PATCHordersorderIdResponse200DataRelationshipsAvailableFreeSkusDataType(str, Enum):
    AVAILABLE_FREE_SKUS = "available_free_skus"

    def __str__(self) -> str:
        return str(self.value)
