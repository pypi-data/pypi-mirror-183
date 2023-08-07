from enum import Enum


class GETcustomerscustomerIdResponse200DataRelationshipsCustomerGroupDataType(str, Enum):
    CUSTOMER_GROUP = "customer_group"

    def __str__(self) -> str:
        return str(self.value)
