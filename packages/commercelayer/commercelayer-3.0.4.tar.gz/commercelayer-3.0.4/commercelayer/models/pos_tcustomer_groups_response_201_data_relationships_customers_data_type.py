from enum import Enum


class POSTcustomerGroupsResponse201DataRelationshipsCustomersDataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
