from enum import Enum


class SkuListDataRelationshipsCustomerDataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
