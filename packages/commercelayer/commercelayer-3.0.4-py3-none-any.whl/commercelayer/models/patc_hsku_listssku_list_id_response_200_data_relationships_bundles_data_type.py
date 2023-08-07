from enum import Enum


class PATCHskuListsskuListIdResponse200DataRelationshipsBundlesDataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
