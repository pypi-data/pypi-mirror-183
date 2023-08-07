from enum import Enum


class GETcustomersResponse200DataItemType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
