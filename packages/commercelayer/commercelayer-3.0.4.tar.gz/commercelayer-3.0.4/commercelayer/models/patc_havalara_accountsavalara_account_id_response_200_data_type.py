from enum import Enum


class PATCHavalaraAccountsavalaraAccountIdResponse200DataType(str, Enum):
    AVALARA_ACCOUNTS = "avalara_accounts"

    def __str__(self) -> str:
        return str(self.value)
