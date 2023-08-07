from enum import Enum


class GETexternalPaymentsResponse200DataItemRelationshipsWalletDataType(str, Enum):
    WALLET = "wallet"

    def __str__(self) -> str:
        return str(self.value)
