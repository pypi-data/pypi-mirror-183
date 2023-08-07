from enum import Enum


class OrderUpdateDataRelationshipsBillingAddressDataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
