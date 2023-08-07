from enum import Enum


class GETpackagespackageIdResponse200DataType(str, Enum):
    PACKAGES = "packages"

    def __str__(self) -> str:
        return str(self.value)
