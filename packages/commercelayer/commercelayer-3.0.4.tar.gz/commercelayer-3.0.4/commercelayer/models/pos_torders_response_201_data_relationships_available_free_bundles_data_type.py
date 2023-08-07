from enum import Enum


class POSTordersResponse201DataRelationshipsAvailableFreeBundlesDataType(str, Enum):
    AVAILABLE_FREE_BUNDLES = "available_free_bundles"

    def __str__(self) -> str:
        return str(self.value)
