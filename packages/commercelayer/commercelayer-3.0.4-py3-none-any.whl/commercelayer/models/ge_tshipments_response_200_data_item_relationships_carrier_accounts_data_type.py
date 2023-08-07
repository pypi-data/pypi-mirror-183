from enum import Enum


class GETshipmentsResponse200DataItemRelationshipsCarrierAccountsDataType(str, Enum):
    CARRIER_ACCOUNTS = "carrier_accounts"

    def __str__(self) -> str:
        return str(self.value)
