from enum import Enum


class GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletDataType(str, Enum):
    WALLET = "wallet"

    def __str__(self) -> str:
        return str(self.value)
