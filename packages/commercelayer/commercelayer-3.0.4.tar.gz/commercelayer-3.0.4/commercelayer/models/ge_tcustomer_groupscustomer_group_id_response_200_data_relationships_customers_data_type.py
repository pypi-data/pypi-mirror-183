from enum import Enum


class GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomersDataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
