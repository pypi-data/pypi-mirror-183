from enum import Enum


class TaxjarAccountDataType(str, Enum):
    TAXJAR_ACCOUNTS = "taxjar_accounts"

    def __str__(self) -> str:
        return str(self.value)
