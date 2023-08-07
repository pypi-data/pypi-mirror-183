from enum import Enum


class GETcustomerGroupsResponse200DataItemRelationshipsCustomersDataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
