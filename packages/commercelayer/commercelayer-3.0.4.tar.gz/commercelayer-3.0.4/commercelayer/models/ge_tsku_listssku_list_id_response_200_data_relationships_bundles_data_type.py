from enum import Enum


class GETskuListsskuListIdResponse200DataRelationshipsBundlesDataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
