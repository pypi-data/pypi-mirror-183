from enum import Enum


class POSTexternalPaymentsResponse201DataRelationshipsWalletDataType(str, Enum):
    WALLET = "wallet"

    def __str__(self) -> str:
        return str(self.value)
