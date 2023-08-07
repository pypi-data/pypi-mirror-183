from enum import Enum


class GETbundlesbundleIdResponse200DataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
