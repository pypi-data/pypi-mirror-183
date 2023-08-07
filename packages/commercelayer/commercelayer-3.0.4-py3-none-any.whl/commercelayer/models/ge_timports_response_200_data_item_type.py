from enum import Enum


class GETimportsResponse200DataItemType(str, Enum):
    IMPORTS = "imports"

    def __str__(self) -> str:
        return str(self.value)
