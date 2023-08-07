from enum import Enum


class POSTcustomerAddressesResponse201DataType(str, Enum):
    CUSTOMER_ADDRESSES = "customer_addresses"

    def __str__(self) -> str:
        return str(self.value)
