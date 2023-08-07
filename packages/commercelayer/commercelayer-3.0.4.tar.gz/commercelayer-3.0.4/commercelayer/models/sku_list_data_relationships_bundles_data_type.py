from enum import Enum


class SkuListDataRelationshipsBundlesDataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
