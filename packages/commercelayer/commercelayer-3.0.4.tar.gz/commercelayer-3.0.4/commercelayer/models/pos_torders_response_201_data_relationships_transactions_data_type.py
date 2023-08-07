from enum import Enum


class POSTordersResponse201DataRelationshipsTransactionsDataType(str, Enum):
    TRANSACTIONS = "transactions"

    def __str__(self) -> str:
        return str(self.value)
