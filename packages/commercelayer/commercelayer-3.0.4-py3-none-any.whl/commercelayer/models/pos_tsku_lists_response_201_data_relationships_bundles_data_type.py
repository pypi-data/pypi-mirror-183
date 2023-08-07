from enum import Enum


class POSTskuListsResponse201DataRelationshipsBundlesDataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
