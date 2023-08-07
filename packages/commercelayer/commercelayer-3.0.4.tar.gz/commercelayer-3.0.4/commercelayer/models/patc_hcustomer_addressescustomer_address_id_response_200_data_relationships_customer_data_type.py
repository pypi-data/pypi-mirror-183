from enum import Enum


class PATCHcustomerAddressescustomerAddressIdResponse200DataRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
