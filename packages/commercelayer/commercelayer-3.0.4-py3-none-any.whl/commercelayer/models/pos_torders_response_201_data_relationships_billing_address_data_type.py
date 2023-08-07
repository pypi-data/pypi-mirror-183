from enum import Enum


class POSTordersResponse201DataRelationshipsBillingAddressDataType(str, Enum):
    BILLING_ADDRESS = "billing_address"

    def __str__(self) -> str:
        return str(self.value)
