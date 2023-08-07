from enum import Enum


class PATCHtaxjarAccountstaxjarAccountIdResponse200DataType(str, Enum):
    TAXJAR_ACCOUNTS = "taxjar_accounts"

    def __str__(self) -> str:
        return str(self.value)
