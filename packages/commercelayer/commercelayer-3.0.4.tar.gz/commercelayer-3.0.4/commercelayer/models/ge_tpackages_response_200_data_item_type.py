from enum import Enum


class GETpackagesResponse200DataItemType(str, Enum):
    PACKAGES = "packages"

    def __str__(self) -> str:
        return str(self.value)
