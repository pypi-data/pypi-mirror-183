from enum import Enum


class GETcustomersResponse200DataItemRelationshipsCustomerGroupDataType(str, Enum):
    CUSTOMER_GROUP = "customer_group"

    def __str__(self) -> str:
        return str(self.value)
