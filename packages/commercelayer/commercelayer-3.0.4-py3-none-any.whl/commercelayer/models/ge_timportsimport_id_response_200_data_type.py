from enum import Enum


class GETimportsimportIdResponse200DataType(str, Enum):
    IMPORTS = "imports"

    def __str__(self) -> str:
        return str(self.value)
