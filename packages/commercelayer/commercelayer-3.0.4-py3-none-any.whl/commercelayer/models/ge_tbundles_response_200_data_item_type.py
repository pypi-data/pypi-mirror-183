from enum import Enum


class GETbundlesResponse200DataItemType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
