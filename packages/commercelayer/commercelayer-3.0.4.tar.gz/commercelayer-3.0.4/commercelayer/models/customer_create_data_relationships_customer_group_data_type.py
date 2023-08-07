from enum import Enum


class CustomerCreateDataRelationshipsCustomerGroupDataType(str, Enum):
    CUSTOMER_GROUPS = "customer_groups"

    def __str__(self) -> str:
        return str(self.value)
