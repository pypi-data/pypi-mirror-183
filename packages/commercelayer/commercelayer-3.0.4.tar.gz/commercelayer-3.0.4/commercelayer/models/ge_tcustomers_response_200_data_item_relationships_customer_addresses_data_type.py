from enum import Enum


class GETcustomersResponse200DataItemRelationshipsCustomerAddressesDataType(str, Enum):
    CUSTOMER_ADDRESSES = "customer_addresses"

    def __str__(self) -> str:
        return str(self.value)
