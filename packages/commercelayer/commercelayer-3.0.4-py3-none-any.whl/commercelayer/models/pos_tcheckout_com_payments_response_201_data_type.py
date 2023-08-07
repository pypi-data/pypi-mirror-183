from enum import Enum


class POSTcheckoutComPaymentsResponse201DataType(str, Enum):
    CHECKOUT_COM_PAYMENTS = "checkout_com_payments"

    def __str__(self) -> str:
        return str(self.value)
