from enum import Enum


class GETshipmentsResponse200DataItemType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
