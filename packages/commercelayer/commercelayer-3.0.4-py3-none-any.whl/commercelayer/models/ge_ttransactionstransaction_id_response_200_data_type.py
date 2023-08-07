from enum import Enum


class GETtransactionstransactionIdResponse200DataType(str, Enum):
    TRANSACTIONS = "transactions"

    def __str__(self) -> str:
        return str(self.value)
