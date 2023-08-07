from enum import Enum


class POSTcustomersResponse201DataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
