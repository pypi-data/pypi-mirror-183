from enum import Enum


class PATCHordersorderIdResponse200DataRelationshipsTransactionsDataType(str, Enum):
    TRANSACTIONS = "transactions"

    def __str__(self) -> str:
        return str(self.value)
