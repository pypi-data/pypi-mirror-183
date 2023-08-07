from enum import Enum


class TransactionDataType(str, Enum):
    TRANSACTIONS = "transactions"

    def __str__(self) -> str:
        return str(self.value)
