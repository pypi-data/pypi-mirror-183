from enum import Enum


class PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletDataType(str, Enum):
    WALLET = "wallet"

    def __str__(self) -> str:
        return str(self.value)
