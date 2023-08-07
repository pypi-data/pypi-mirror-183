from enum import Enum


class CustomerGroupDataRelationshipsCustomersDataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
