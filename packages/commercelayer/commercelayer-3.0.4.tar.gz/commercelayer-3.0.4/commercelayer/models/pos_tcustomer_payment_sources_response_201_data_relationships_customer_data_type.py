from enum import Enum


class POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
