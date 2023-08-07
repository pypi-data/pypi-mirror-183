from enum import Enum


class CustomerAddressCreateDataType(str, Enum):
    CUSTOMER_ADDRESSES = "customer_addresses"

    def __str__(self) -> str:
        return str(self.value)
