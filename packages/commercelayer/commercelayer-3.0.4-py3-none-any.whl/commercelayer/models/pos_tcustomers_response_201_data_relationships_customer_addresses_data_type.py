from enum import Enum


class POSTcustomersResponse201DataRelationshipsCustomerAddressesDataType(str, Enum):
    CUSTOMER_ADDRESSES = "customer_addresses"

    def __str__(self) -> str:
        return str(self.value)
