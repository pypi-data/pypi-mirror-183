from enum import Enum


class POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsDataType(str, Enum):
    KLARNA_PAYMENTS = "klarna_payments"

    def __str__(self) -> str:
        return str(self.value)
