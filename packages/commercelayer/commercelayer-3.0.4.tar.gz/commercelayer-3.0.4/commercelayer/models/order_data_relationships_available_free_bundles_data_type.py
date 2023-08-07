from enum import Enum


class OrderDataRelationshipsAvailableFreeBundlesDataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
