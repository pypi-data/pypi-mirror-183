from enum import Enum


class POSTordersResponse201DataRelationshipsAvailableCustomerPaymentSourcesDataType(str, Enum):
    AVAILABLE_CUSTOMER_PAYMENT_SOURCES = "available_customer_payment_sources"

    def __str__(self) -> str:
        return str(self.value)
