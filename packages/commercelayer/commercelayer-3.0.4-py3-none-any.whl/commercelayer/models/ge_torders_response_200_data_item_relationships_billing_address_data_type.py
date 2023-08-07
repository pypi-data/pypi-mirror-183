from enum import Enum


class GETordersResponse200DataItemRelationshipsBillingAddressDataType(str, Enum):
    BILLING_ADDRESS = "billing_address"

    def __str__(self) -> str:
        return str(self.value)
