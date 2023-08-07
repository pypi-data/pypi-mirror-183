from enum import Enum


class GETcustomerGroupscustomerGroupIdResponse200DataType(str, Enum):
    CUSTOMER_GROUPS = "customer_groups"

    def __str__(self) -> str:
        return str(self.value)
