from enum import Enum


class GETtaxjarAccountstaxjarAccountIdResponse200DataType(str, Enum):
    TAXJAR_ACCOUNTS = "taxjar_accounts"

    def __str__(self) -> str:
        return str(self.value)
