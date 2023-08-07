from enum import Enum


class GETcarrierAccountscarrierAccountIdResponse200DataType(str, Enum):
    CARRIER_ACCOUNTS = "carrier_accounts"

    def __str__(self) -> str:
        return str(self.value)
