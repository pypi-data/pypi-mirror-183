from enum import Enum


class POSTinStockSubscriptionsResponse201DataRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
