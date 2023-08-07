from enum import Enum


class GETreturnsreturnIdResponse200DataRelationshipsOrderDataType(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
