from enum import Enum


class GETcustomerscustomerIdResponse200DataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
