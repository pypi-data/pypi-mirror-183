from enum import Enum


class OrderDataRelationshipsBillingAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
