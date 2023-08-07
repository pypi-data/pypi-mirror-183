from enum import Enum


class POSTcustomerPasswordResetsResponse201DataRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
