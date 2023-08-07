from enum import Enum


class GETpromotionspromotionIdResponse200DataType(str, Enum):
    PROMOTIONS = "promotions"

    def __str__(self) -> str:
        return str(self.value)
