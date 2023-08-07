from enum import Enum


class POSTtaxjarAccountsResponse201DataType(str, Enum):
    TAXJAR_ACCOUNTS = "taxjar_accounts"

    def __str__(self) -> str:
        return str(self.value)
