from enum import Enum


class PATCHpackagespackageIdResponse200DataType(str, Enum):
    PACKAGES = "packages"

    def __str__(self) -> str:
        return str(self.value)
