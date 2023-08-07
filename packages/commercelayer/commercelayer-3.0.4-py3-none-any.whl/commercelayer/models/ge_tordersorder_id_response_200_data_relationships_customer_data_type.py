from enum import Enum


class GETordersorderIdResponse200DataRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
