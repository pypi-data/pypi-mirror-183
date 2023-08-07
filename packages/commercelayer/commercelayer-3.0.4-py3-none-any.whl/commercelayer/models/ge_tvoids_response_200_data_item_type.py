from enum import Enum


class GETvoidsResponse200DataItemType(str, Enum):
    VOIDS = "voids"

    def __str__(self) -> str:
        return str(self.value)
