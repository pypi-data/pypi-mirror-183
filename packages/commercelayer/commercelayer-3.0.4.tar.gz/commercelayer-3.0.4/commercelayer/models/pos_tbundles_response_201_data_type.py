from enum import Enum


class POSTbundlesResponse201DataType(str, Enum):
    BUNDLES = "bundles"

    def __str__(self) -> str:
        return str(self.value)
