from enum import Enum


class PATCHcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomersDataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
