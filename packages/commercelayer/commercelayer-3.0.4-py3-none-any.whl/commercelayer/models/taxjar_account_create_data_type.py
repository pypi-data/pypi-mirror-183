from enum import Enum


class TaxjarAccountCreateDataType(str, Enum):
    TAXJAR_ACCOUNTS = "taxjar_accounts"

    def __str__(self) -> str:
        return str(self.value)
