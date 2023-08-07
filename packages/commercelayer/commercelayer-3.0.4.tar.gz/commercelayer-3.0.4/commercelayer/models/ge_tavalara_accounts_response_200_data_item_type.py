from enum import Enum


class GETavalaraAccountsResponse200DataItemType(str, Enum):
    AVALARA_ACCOUNTS = "avalara_accounts"

    def __str__(self) -> str:
        return str(self.value)
