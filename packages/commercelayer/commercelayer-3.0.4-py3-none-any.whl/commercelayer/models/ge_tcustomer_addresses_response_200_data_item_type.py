from enum import Enum


class GETcustomerAddressesResponse200DataItemType(str, Enum):
    CUSTOMER_ADDRESSES = "customer_addresses"

    def __str__(self) -> str:
        return str(self.value)
