from enum import Enum


class POSTcustomerGroupsResponse201DataType(str, Enum):
    CUSTOMER_GROUPS = "customer_groups"

    def __str__(self) -> str:
        return str(self.value)
