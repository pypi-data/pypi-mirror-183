from enum import Enum


class POSTimportsResponse201DataType(str, Enum):
    IMPORTS = "imports"

    def __str__(self) -> str:
        return str(self.value)
