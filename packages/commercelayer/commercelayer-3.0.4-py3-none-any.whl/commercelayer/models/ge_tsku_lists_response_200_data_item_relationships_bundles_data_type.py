from enum import Enum


class GETskuListsResponse200DataItemRelationshipsBundlesDataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
