from enum import Enum


class AvalaraAccountUpdateDataType(str, Enum):
    AVALARA_ACCOUNTS = "avalara_accounts"

    def __str__(self) -> str:
        return str(self.value)
