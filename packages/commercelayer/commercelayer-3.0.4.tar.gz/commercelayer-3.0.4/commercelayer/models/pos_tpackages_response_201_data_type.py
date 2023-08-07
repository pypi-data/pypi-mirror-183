from enum import Enum


class POSTpackagesResponse201DataType(str, Enum):
    PACKAGES = "packages"

    def __str__(self) -> str:
        return str(self.value)
