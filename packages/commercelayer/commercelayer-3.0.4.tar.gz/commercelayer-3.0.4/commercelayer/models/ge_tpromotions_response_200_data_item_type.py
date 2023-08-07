from enum import Enum


class GETpromotionsResponse200DataItemType(str, Enum):
    PROMOTIONS = "promotions"

    def __str__(self) -> str:
        return str(self.value)
