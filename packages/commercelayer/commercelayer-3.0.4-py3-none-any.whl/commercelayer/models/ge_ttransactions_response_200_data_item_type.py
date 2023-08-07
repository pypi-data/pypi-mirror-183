from enum import Enum


class GETtransactionsResponse200DataItemType(str, Enum):
    TRANSACTIONS = "transactions"

    def __str__(self) -> str:
        return str(self.value)
