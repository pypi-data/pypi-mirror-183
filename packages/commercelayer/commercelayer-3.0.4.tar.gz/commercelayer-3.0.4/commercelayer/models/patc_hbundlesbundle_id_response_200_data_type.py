from enum import Enum


class PATCHbundlesbundleIdResponse200DataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
