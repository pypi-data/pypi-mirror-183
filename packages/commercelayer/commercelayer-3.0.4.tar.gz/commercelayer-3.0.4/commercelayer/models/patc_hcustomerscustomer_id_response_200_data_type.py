from enum import Enum


class PATCHcustomerscustomerIdResponse200DataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
