from enum import Enum


class GETordersResponse200DataItemRelationshipsTransactionsDataType(str, Enum):
    TRANSACTIONS = "transactions"

    def __str__(self) -> str:
        return str(self.value)
